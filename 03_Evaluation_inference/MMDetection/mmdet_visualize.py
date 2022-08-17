# -*- coding: utf-8 -*-
import argparse
from pathlib import Path
# import matplotlib.pyplot as plt
import pickle
# import os
# import cv2

import mmcv
from mmcv.runner import load_checkpoint

from mmdet.apis import inference_detector, show_result_pyplot
from mmdet.models import build_detector

def save_pickle(obj, fn):
    with open(str(fn), 'wb') as f:
        pickle.dump(obj, f)

parser = argparse.ArgumentParser(
    description='MMDet test (and eval) a model')
parser.add_argument('config', help='test config file path')
parser.add_argument('checkpoint', help='checkpoint file')
parser.add_argument(
    '--output-dir',
    help='the directory to save results')
parser.add_argument(
        '--images',
        nargs='+')
args = parser.parse_args()

device = 'cpu'
config = mmcv.Config.fromfile(args.config)
# Set pretrained to be None since we do not need pretrained model here
#config.model.pretrained = None

# Initialize the detector
model = build_detector(config.model)

# Load checkpoint
checkpoint = load_checkpoint(model, args.checkpoint, map_location=device)

# Set the classes of models for inference
model.CLASSES = checkpoint['meta']['CLASSES']

# We need to set the model's cfg for inference
model.cfg = config

# Convert the model to GPU
model.to(device)
# Convert the model into evaluation mode
model.eval()


output_dir = Path(args.output_dir)
output_dir.mkdir(exist_ok=True, parents=True)
for image_fn in args.images:
    result = inference_detector(model, image_fn)
#    save_pickle(result, output_dir / f'{Path(image_fn).stem}.pkl')
    show_result_pyplot(
        model, image_fn, result, score_thr=0.3,
        out_file=str(output_dir / f'{Path(image_fn).stem}.png'))



