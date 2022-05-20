# MMDetection

[MMDetection](https://github.com/open-mmlab/mmdetection) is an object detection toolbox.

Some key advantages:
- modular design
- config-based run
- modern neural networks architectures
- training technics, losses, logging etc implemented (including modern augmentation, test time augmentation, loss smoothing, warmup)
- member of larger family https://openmmlab.com/codebase

## Usage

Usage of MMDetecion is documented here: https://mmdetection.readthedocs.io

As an alternative to `train.py` script provided in the offial repository, you may use our `mmdet_train.py` script included in `tools` directory.
It accepts multiple config files as an argument, what allows you to keep configuration files of datasets and training rutines separately and use them in a modular way.

Example:
```python
python tools/mmdet_train.py {mmdetection_repository}/configs/faster_rcnn/faster_rcnn_r101_caffe_fpn_1x_coco.py \
        sample_configs/data_chess_config.py \
        sample_configs/run_config.py \
        --cfg-options work_dir="./mmdet_outupt/chess_01"
```
for another dataset but with the same settings except for number of epochs increased to 50:
```python
python tools/mmdet_train.py {mmdetection_repository}/configs/faster_rcnn/faster_rcnn_r101_caffe_fpn_1x_coco.py \
        {path-to-my-project}/{another-data-config}.py \
        sample_configs/run_config.py \
        --cfg-options work_dir="./mmdet_outupt/another_project_01" \
        runner.max_epochs=50
```


## Docker

MMDetection repository comes with a [Dockerfile](https://github.com/open-mmlab/mmdetection/blob/master/docker/Dockerfile)

Already build Docker image, enriched with Tensorboard, is available here: https://hub.docker.com/r/mbuk/mmdet
