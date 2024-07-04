# Novel camera view rendering of trained Gaussian Splatting model to PNG images

By Pranav Chougule, Arizona State University

Follow Google Colab Notebook to render novel views pretrained model

https://colab.research.google.com/drive/11jayCPkY7Nr9OV9bxzzN3SHjMzb2poS6?usp=sharing

directory ```render-input-data\sample-folder```:
```
<sample-folder>
|---images.txt
|---cameras.txt
|---point-cloud.ply
```

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
