# EXPERIMENT OF PRANAV CHOUGULE
# Copyright (C) 2023, Inria
# GRAPHDECO research group, https://team.inria.fr/graphdeco
# All rights reserved.
#
# This software is free for non-commercial, research and evaluation use 
# under the terms of the LICENSE.md file.
#
# For inquiries contact  george.drettakis@inria.fr
#

import torch
from scene_nv import Scene
import os
from tqdm import tqdm
from os import makedirs
from gaussian_renderer import render
import torchvision
from utils.general_utils import safe_state
from argparse import ArgumentParser
from arguments_nv import ModelParams, PipelineParams, get_combined_args
from gaussian_renderer import GaussianModel

def render_set(model_path, name, iteration, views, gaussians, pipeline, background):
    render_path = os.path.join(model_path,"renders")
    # gts_path = os.path.join(model_path, name, "ours_{}".format(iteration), "gt") # GT isnt present for Unknown poses (P.V.C.A.P)

    makedirs(render_path, exist_ok=True)
    # makedirs(gts_path, exist_ok=True) # GT isnt present for Unknown poses (P.V.C.A.P)

    # print(views) (P.V.C.A.P)

    for idx, view in enumerate(tqdm(views, desc="Rendering progress")):

        # # print(dir(view)) #(P.V.C.A.P)

        # print("FoVx:", view.FoVx, "Type:", type(view.FoVx)) #(P.V.C.A.P)
        # print("FoVy:", view.FoVy, "Type:", type(view.FoVy)) #(P.V.C.A.P)
        # print("image_height:", view.image_height, "Type:", type(view.image_height)) #(P.V.C.A.P)
        # print("image_width:", view.image_width, "Type:", type(view.image_width)) #(P.V.C.A.P)
        # print("world_view_transform:", view.world_view_transform, "Type:", type(view.world_view_transform)) #(P.V.C.A.P)
        # print("full_proj_transform:", view.full_proj_transform, "Type:", type(view.full_proj_transform)) #(P.V.C.A.P)
        # print("camera_center:", view.camera_center, "Type:", type(view.camera_center)) #(P.V.C.A.P)

        rendering = render(view, gaussians, pipeline, background)["render"]  #(L.T.W.O.F)
        # gt = view.original_image[0:3, :, :] #No need of GT for unknown camera poses it doesnt exist (P.V.C.A.P)
        torchvision.utils.save_image(rendering, os.path.join(render_path, '{0:05d}'.format(idx) + ".png"))
        # torchvision.utils.save_image(gt, os.path.join(gts_path, '{0:05d}'.format(idx) + ".png")) #No need of GT for unknown camera poses it doesnt exist (P.V.C.A.P)

def render_sets(dataset : ModelParams, iteration : int, pipeline : PipelineParams, skip_train : bool, skip_test : bool):
    with torch.no_grad():
        gaussians = GaussianModel(dataset.sh_degree)
        scene = Scene(dataset, gaussians, load_iteration=iteration, shuffle=False)
        # Print data type and details about train_cameras
        # train_cameras = scene.getTrainCameras()
        # print(f"Type: {type(train_cameras)}, Size: {len(train_cameras)}")
        # print(train_cameras)
        
        # if len(train_cameras) > 0:
        #     for i, camera in enumerate(train_cameras):
        #         print(f"\nCamera {i} attributes:")
        #         for attr_name, attr_value in vars(camera).items():
        #             print(f"{attr_name}: {attr_value} Type: {type(attr_value)}")

        bg_color = [1,1,1] if dataset.white_background else [0, 0, 0]
        background = torch.tensor(bg_color, dtype=torch.float32, device="cuda")

        if not skip_train:
             render_set(dataset.model_path, "train", scene.loaded_iter, scene.getTrainCameras(), gaussians, pipeline, background) #(L.T.W.O.F)

        if not skip_test:
             render_set(dataset.model_path, "test", scene.loaded_iter, scene.getTestCameras(), gaussians, pipeline, background)

if __name__ == "__main__":
    # Set up command line argument parser
    parser = ArgumentParser(description="Testing script parameters")
    model = ModelParams(parser, sentinel=True)
    pipeline = PipelineParams(parser)
    parser.add_argument("--iteration", default=-1, type=int)
    parser.add_argument("--skip_train", action="store_true")
    parser.add_argument("--skip_test", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    args = get_combined_args(parser)
    print("Rendering " + args.model_path)

    # Initialize system state (RNG)
    safe_state(args.quiet)

    render_sets(model.extract(args), args.iteration, pipeline.extract(args), args.skip_train, args.skip_test)