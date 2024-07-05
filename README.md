# Novel camera view rendering of trained Gaussian Splatting model to PNG images
By Pranav Chougule, Arizona State University.

Welcome to the enhanced version of the 3D Gaussian Splatting for Real-Time Radiance Field Rendering project! This repository extends the original project’s capabilities, providing greater flexibility and functionality for rendering 3D scenes.

## Overview
This enhanced repository introduces a crucial new capability: the ability to generate novel synthetic views from user-defined camera poses. Unlike the original project, which was limited to rendering views from predetermined camera poses generated via COLMAP, this version allows you to specify arbitrary camera positions and orientations. This significantly expands the versatility and application of the Gaussian splatting technique.

## Key Features
- Novel View Synthesis: Define your own camera poses to generate new, synthetic views of the 3D scene, offering more creative control and flexibility.
- Original Functionality: Retains all features from the original repository, including radiance field rendering from ground truth images.
- Seamless Integration: The new capabilities are seamlessly integrated into the existing workflow, making it easy to leverage both the original and enhanced features.

## Applications
This powerful capability facilitates various advanced applications, including:
Extended Reality (XR): Create immersive XR experiences with dynamic viewpoints, enhancing user engagement and interactivity.
Photogrammetry on Synthetic Views: Generate synthetic views for photogrammetry, enabling the creation of dense texture-mapped 3D models from novel perspectives.
Simulated SLAM: Conduct simulated SLAM (Simultaneous Localization and Mapping) for robotic or autonomous vehicle simulations, providing diverse and customizable environments for testing.

## Google Colab Notebook for rendering novel views
To get started quickly, follow [here](https://colab.research.google.com/drive/11jayCPkY7Nr9OV9bxzzN3SHjMzb2poS6?usp=sharing/) for step-by-step instructions on rendering novel views using a pre-trained model.

## Cloning the Repository and setting up the environment
I used a fork from https://github.com/jonstephens85/gaussian-splatting-Windows.git to clone the Gaussian Splatting repo in Windows 11. It has some issues, and by addressing them, I arrived at the following software versions. Although you can download Git, Conda, Colmap, FFMPEG, and ImageMagik from the above repo's links.
- CUDA 11.7 (Recommended CUDA 11.8 has some issues with this repo)
- Visual Studio 2019 (April-June 2024 update of Visual Code 2022 is not working)

To clone this repository, use the following command:

```bash
git clone https://github.com/pranavc2255/gaussian-splatting-novel-view-render --recursive
```
My conda environment can be installed by the following command which I used for COLMAP and Rendering (I used Colab for training the Gaussian Splatting Model Since I only had 4GB VRAM GTX 3050): 

```bash
conda env create -f environment_nv.yml
```

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

python render_nv.py --model_path /content/drive/MyDrive/Gaussian-Splatting-render/gaussian-splatting-novel-view-render/render-input-data/sample-folder/ --source_path /content/drive/MyDrive/Gaussian-Splatting-render/gaussian-splatting-novel-view-render/render-input-data/sample-folder
```
I have used the same path for my model and source folder in the Google Colab file.
If you wish to have different paths for the model and source, you can do so by using the below cmd line.
```shell

python render_nv.py --model_path <path to point-cloud.ply (pre-trained model)> --source_path <path to images.txt and cameras.txt>
```
## Instructions for Creating and Formatting images.txt and cameras.txt
### images.txt Format
 Each line corresponds to one camera pose and includes the following information:
- **NOVEL_CAMERA_POSE_ID**: A unique identifier for the camera pose.
- **QW, QX, QY, QZ**: The quaternion components representing the orientation of the camera 
- **TX, TY, TZ**: The translation vector components representing the position of the camera.
### cameras.txt Format
Each line corresponds to one camera model and includes the following information:
- **CAMERA_ID**: A unique identifier for the camera model.
- **MODEL**: The camera model type. Only PINHOLE or SIMPLE_PINHOLE models are supported.
- **WIDTH**: The width resolution of the images.
- **HEIGHT**: The height resolution of the images.
- **PARAMS[]**: The camera parameters-
   - **For PINHOLE**: focal_length_x, focal_length_y, principal_point_x,   
                   principal_point_y
   - **For SIMPLE_PINHOLE**: focal_length, principal_point_x, principal_point_y
## References

If you want to train a new model, follow the instructions provided in the [original Gaussian Splatting repository](https://github.com/graphdeco-inria/gaussian-splatting/). It includes detailed steps and necessary scripts for training on your dataset.
