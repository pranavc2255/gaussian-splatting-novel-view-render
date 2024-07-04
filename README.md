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

```shell
## Running the Script
To render novel views, run the render_nv.py script:

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
