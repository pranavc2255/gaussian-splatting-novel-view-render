import camorph.camorph as camorph
import json
import argparse
import os
import subprocess

def main(input_fbx_path,output_colmap_path):

    input_fbx_path = args.input_fbx_path
    output_colmap_path = args.output_colmap_path

    try:
        # Read the camera parameters from the FBX file
        cameras = camorph.read_cameras('fbx', input_fbx_path)
        print("Successfully read camera parameters from FBX file.")

        # Visualize the cameras (optional)
        # camorph.visualize(cameras)
        # print("Camera visualization complete.")

        # Write the camera parameters to the COLMAP format
        camorph.write_cameras('COLMAP', output_colmap_path, cameras)
        print("Successfully wrote camera parameters to COLMAP format.")

    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        print("There was an error reading the FBX file. Please check the file encoding or try another file.")
        
        # Attempt to re-encode the FBX file using a different method
        import fbx


        manager = fbx.FbxManager.Create()
        importer = fbx.FbxImporter.Create(manager, "")

        # Load the scene from the FBX file
        status = importer.Initialize(input_fbx_path, -1, manager.GetIOSettings())
        if not status:
            print("Failed to initialize FBX importer.")
        else:
            scene = fbx.FbxScene.Create(manager, "scene")
            importer.Import(scene)
            importer.Destroy()

            # Export the scene to a new FBX file with proper encoding
            output_fbx_temp_path = './temp_exported_circular_path.fbx'
            exporter = fbx.FbxExporter.Create(manager, "")
            status = exporter.Initialize(output_fbx_temp_path, -1, manager.GetIOSettings())
            if not status:
                print("Failed to initialize FBX exporter.")
            else:
                exporter.Export(scene)
                exporter.Destroy()
                print(f"Re-encoded FBX file saved to: {output_fbx_temp_path}")
                
                # Try reading the re-encoded FBX file with camorph
                cameras = camorph.read_cameras('fbx', output_fbx_temp_path)
                camorph.visualize(cameras)
                camorph.write_cameras('COLMAP', output_colmap_path, cameras)
                print("Successfully wrote camera parameters to COLMAP format using re-encoded FBX file.")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        print("The specified file was not found. Please check the file path and try again.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        config_path = './config.json'

        try:
            # Load the config file
            with open(config_path, 'r') as config_file:
                config = json.load(config_file)

            # Read the camera parameters from the FBX file
            cameras = camorph.read_cameras('fbx', input_fbx_path)
            print("Successfully read camera parameters from FBX file.")

            # Visualize the cameras (optional)
            #camorph.visualize(cameras)
            #print("Camera visualization complete.")

            # Set missing properties from the config file or use default values
            for camera in cameras:
                camera_name = camera.name  # Use the attribute directly instead of calling it as a function
                camera_config = next((item for item in config['values'] if item['name'] == camera_name), {})
                camera.source_image = camera_config.get('source_image', 'placeholder_image.png')
                camera.resolution = camera_config.get('resolution', [6240, 4160])
                camera.sensor_size = camera_config.get('sensor_size', [36, 24])
                camera.focal_length = camera_config.get('focal_length', 35)

            # Write the camera parameters to the COLMAP format
            camorph.write_cameras('COLMAP', output_colmap_path, cameras)
            print("Successfully wrote camera parameters to COLMAP format.")

        except UnicodeDecodeError as e:
                print(f"UnicodeDecodeError: {e}")
                print("There was an error reading the FBX file. Please check the file encoding or try another file.")

        except FileNotFoundError as e:
                print(f"FileNotFoundError: {e}")
                print("The specified file was not found. Please check the file path and try again.")

        except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert camera parameters from FBX to COLMAP format and extract headers.")
    parser.add_argument('-f', '--input_fbx_path', type=str, required=True, help='Path to the input FBX file.')
    parser.add_argument('-c', '--output_colmap_path', type=str, required=True, help='Path to the output COLMAP directory.')

    args = parser.parse_args()


    # Run the main function of script2.py
    main(args.input_fbx_path, args.output_colmap_path)

    # Run script1.py with subprocess
    subprocess.run(["python", "convert_txt_nv.py", "--input", args.output_colmap_path, "--output", args.output_colmap_path])