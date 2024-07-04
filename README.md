# Novel camera view rendering of trained Gaussian Splatting model to PNG images

By Pranav Chougule, Arizona State University
## Overview
Gaussian Splatting is a technique for rendering novel views of a scene using a point cloud representation. This repository includes scripts and sample data to demonstrate how to render images from different viewpoints using a trained Gaussian splatting model.
## Google Colab Notebook
To get started quickly, follow [here](https://colab.research.google.com/drive/11jayCPkY7Nr9OV9bxzzN3SHjMzb2poS6?usp=sharing/) for step-by-step instructions on rendering novel views using a pretrained model.

## Directory Structure for sample data
Ensure your directory structure is as follows:

directory ```render-input-data\sample-folder```:
```
<sample-folder>
|---images.txt
|---cameras.txt
|---point-cloud.ply
```
## Running the Script
To render novel views, run the render_nv.py script:
 
```shell

!python render_nv.py --model_path /content/drive/MyDrive/Gaussian-Splatting-render/gaussian-splatting-novel-view-render/render-input-data/sample-folder/ --source_path /content/drive/MyDrive/Gaussian-Splatting-render/gaussian-splatting-novel-view-render/render-input-data/sample-folder
```
I have used the same path for my model and source folder in the google colab file.
If you wish to have different paths for the model and source, you can do so by using the below cmd line.
```shell

python render_nv.py --model_path <path to point-cloud.ply (pre-trained model)> --source_path <path to images.txt and cameras.txt>
```
## Instructions for Creating and Formatting images.txt and cameras.txt
### images.txt Format
 Each line corresponds to one camera pose and includes the following information:
- NOVEL_CAMERA_POSE_ID: A unique identifier for the camera pose.
- QW, QX, QY, QZ: The quaternion components representing the orientation of the camera 
- TX, TY, TZ: The translation vector components representing the position of the camera.
### cameras.txt Format
Each line corresponds to one camera model and includes the following information:
- CAMERA_ID: A unique identifier for the camera model.
- MODEL: The camera model type. Only PINHOLE or SIMPLE_PINHOLE models are supported.
- WIDTH: The width resolution of the images.
- HEIGHT: The height resolution of the images.
- PARAMS[]: The camera parameters-
   - For PINHOLE: focal_length_x, focal_length_y, principal_point_x,   
                   principal_point_y
   - For SIMPLE_PINHOLE: focal_length, principal_point_x, principal_point_y
## References

If you want to train a new model, follow the instructions provided in the [original Gaussian Splatting repository](https://github.com/graphdeco-inria/gaussian-splatting/) . It includes detailed steps and necessary scripts for training on your dataset.
