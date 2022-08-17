# View dataset

## Preliminaries
1. This recipe uses ports 8000 and 8001
1. Create Voxel51 docker image from https://github.com/voxel51/fiftyone

## Standard usage
1. Run Voxel51 container in interactive mode:
   ```
   docker run -v /scratch_on_host:/scratch -p 8000:8000 -p 8001:8001 -it voxel51 sh
   ```
2. Run jupyter notebook in `/scratch` directory:
   ```bash
   cd /scratch
   jupyter notebook --no-browser --allow-root --port 8000 --ip 0.0.0.0
   ```
    open the address (`http://127.0.0.1:8000/?token=...`) in web browser

3. open `02_view_dataset/view_coco_dataset.ipynb` notebook and run all cells

4. In local machine, open `http://localhost:8001` in web browser

