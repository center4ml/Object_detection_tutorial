# Run YOLOv5 in container

## Building Docker container
1. clone repository 
   ```
   git clone https://github.com/ultralytics/yolov5.git
   ```
2. walk into the repository
   ```
   cd yolov5
   ```
3. build Docker container
   ```
   docker build -t yolov5:latest -f utils/docker/Dockerfile .
   ```
4. Run container
   ```
   docker run --gpus --it -v $pwd:/scratch
   ```
   (you may want to replace `$pwd` with another directory on the local machine that schould be visible in container in `/scratch` location)
## Building Singularity container for YOLOv5 model

Singularity containers often are used in High Performance Computing (HPC) centers. Singularity container can be build from Docker container. The steps are as follows:

1. Save Docker container in `.tar` file
   ```
   docker image save -o yolov5.tar yolov5:latest
   ```
2. copy `yolov5.tar` to HPC cluster
3. To build a singularity container, you use the `singularity build` command. The singularity container may be created in ICM (or other HPC center) with the following command:
   ```
   singularity build --tmpdir /home/{username}/tmp yolo.sif docker-archive://yolo.tar
   ```

## Running YOLOv5 training in Singularity container

1. In order to run of training you have to set the queue to system `Rysy` ICM:
   ```
   srun -N1 -n4 --account {account number} --gres=gpu:1 --time=48:00:00 --pty /bin/bash -l
   ```

2. To run our new container (run the interactive instance inside container) you use following command:

   ```
   singularity shell --nv yolo.sif
   ```

3. To run the train a YOLOv5 model you use following command:

   ```
   python /usr/src/app/train.py --batch 16 --epochs 5 --data data.yaml --model models/yolov5s.yaml --weights yolov5s.pt --cache --project results
   ```

   where:
   -  `--data` is a data config file (see: https://github.com/ultralytics/yolov5/tree/master/data)
   - `--model` is a path to model config file (see: https://github.com/ultralytics/yolov5/tree/master/models)
   - `--weights` is a path to initial weights
   - `--project` is a path to directory where training output will be stored

4. Once we have tested the training works, we can run the training with a SLURM script, e.g. `yolo_train.batch`:
   ```
   #!/bin/bash
   #SBATCH --job-name yolo_training # informative
   #SBATCH -A xxxx             # your account or grant name (to be charged for the computations in HPC)
   #SBATCH --time=2-00:00:00   # or whatever fits the QoS, adjust this to match the walltime of your job
   #SBATCH --cpus-per-task=8   
   #SBATCH --gres=gpu:1        # You need to request one GPU
   #SBATCH --mem=90G           # adjust this according to the memory requirement per node you need

   singularity exec --nv yolo.sif python /usr/src/app/train.py {train.py arguments as in the point above}
   ```
   with command:
   ```
   sbatch yolo_train.batch
   ```
