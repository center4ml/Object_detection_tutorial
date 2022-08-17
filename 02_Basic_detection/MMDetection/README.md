# Training

## Docker

MMDetection repository comes with a [Dockerfile](https://github.com/open-mmlab/mmdetection/blob/master/docker/Dockerfile)

Already build Docker image, enriched with Tensorboard, is available here: https://hub.docker.com/r/mbuk/mmdet

## 1. Prepare data pipeline
try `MMDet_pipeline.ipynb` on your data. Choose augmentations and transformations. You may save it to the `pipelines_config.py` and merge it to 

### 2. Prepare config

#### Manually 

By editing config file. Take care of the `_base_` configs, as they are indicated by relative path. IMHO the best way is to create subdirectory in `mmdetection/configs` with your configs.

#### On training time

You can update config entries in the training script arguments (`--cfg-options`) - good solution for small changes

#### Build form pices with `merge_configs.py`

With `tools/merge_configs.py` you can combine multiple config files.

*Example:* Join default model config with configs deterimining dataset (`data_config.py`), data pipeline (`pipelines_config`) and run (`run_config_tb`), update working dir (or other config entries) with `--cfg-options` and save the config under readible name (here `run004.py`)

```bash
python merge_configs.py \
   /mmdetection/configs/mask2former/mask2former_swin-t-p4-w7-224_lsj_8x2_50e_coco.py \
   configs/data_config.py \
   configs/pipelines_config.py \
   configs/run_config_tb.py \
   --cfg-options \
      work_dir=mmdet_outupt/run_004 \
   --out run004.py
```
### 3. Run training

Use `tools/train.py` script from [mmdetection repository](https://github.com/open-mmlab/mmdetection)

Run training from config file. After `--cfg-options` you may override od add some entries in the config

```bash
python tools/train.py \ 
    {config path} \
     --cfg-options \
        work_dir={working_directory} \
        runner.max_iters={num iters} \
        pretrained={checkpoint path} \
        data.workers_per_gpu={} \
        ...
```
