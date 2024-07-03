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
