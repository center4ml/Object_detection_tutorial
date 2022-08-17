# -*- coding: utf-8 -*-

import json
import pickle
import itertools
from unittest.mock import NonCallableMagicMock
import numpy as np
import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description='convert mmdetection results to json')
    parser.add_argument('file_in', help='path  of the input file')
    parser.add_argument('--out',
                        help='path of the output file, default: same as input with json extension',
                        default=None
                        )
    parser.add_argument('--score_thr',
                        help='score belowe which detections are discarded',
                        default=0.1
                        )
    args = parser.parse_args()

    return args

# %% functions from mmdet


def concat_list(in_list):  # from mmcv
    return list(itertools.chain(*in_list))


def proccess_mmdet(result):
    if isinstance(result, tuple):
        bbox_result, segm_result = result
        if isinstance(segm_result, tuple):
            segm_result = segm_result[0]  # ms rcnn
    else:
        bbox_result, segm_result = result, None
    bboxes = np.vstack(bbox_result)
    labels = [
        np.full(bbox.shape[0], i, dtype=np.int32)
        for i, bbox in enumerate(bbox_result)
    ]
    labels = np.concatenate(labels)
    # draw segmentation masks
    segms = None
    if segm_result is not None and len(labels) > 0:  # non empty
        segms = concat_list(segm_result)
        # if isinstance(segms[0], torch.Tensor):
        #     segms = torch.stack(segms, dim=0).detach().cpu().numpy()
        # else:
        segms = np.stack(segms, axis=0)
    else:
        segms = [None]*len(labels)

    return bboxes, labels, segms
# %% main


def main():
    args = parse_args()
    score_thr = args.score_thr

    predictions = pickle.load(open(args.file_in, 'rb'))

    predictions_out = []
    for preds in predictions:
        sample_preds_out = []

        bboxes, labels, masks = proccess_mmdet(preds)
        scores = np.array(bboxes[:, -1]).astype(np.float64)

        if not (scores >= score_thr).any():
            continue

        labels = labels.astype(np.int64)
        boxes = np.array(bboxes[:, :4]).astype(np.float64)

        # save data in close to FiftyOne format
        for label, score, box, mask in zip(labels, scores, boxes, masks):
            if score < score_thr:
                continue
            # x1, y1, x2, y2 = box

            # # x1 = int(np.floor(x1))
            # # x2 = int(np.ceil(x2))
            # # y1 = int(np.floor(y1))
            # # y2 = int(np.ceil(y2))

            # # Convert to [top-left-x, top-left-y, width, height]
            # # in relative coordinates in [0, 1] x [0, 1]
            # rel_box = [x1 / w, y1 / h, (x2 - x1) / w, (y2 - y1) / h]

            # json doesn't accept bytes - convert it to string
            if mask is not None:
                mask['counts'] = mask['counts'].decode()

            sample_preds_out.append({
                'label': int(label),
                'bounding_box': box.tolist(),
                'confidence': score
            })

        predictions_out.append(sample_preds_out)

    path_out = args.out
    if path_out is None:
        path_out = str(Path(args.file_in).with_suffix('.json'))
    with open(path_out, 'w') as f:
        json.dump(predictions_out, f)


# %% run main
if __name__ == '__main__':
    main()
