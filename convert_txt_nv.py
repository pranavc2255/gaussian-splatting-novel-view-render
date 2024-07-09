import re
import argparse
import os
import shutil

def extract_headers(input_dir, output_dir):
    input_file = os.path.join(input_dir, "images.txt")
    print(f"Input file: {input_file}")
    print(f"Output directory: {output_dir}")
    
    with open(input_file, 'r') as file:
        data = file.read()

    # Updated regular expression to match the header information for each image
    pattern = re.compile(r'(\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+\d+)\s+\S+\.\w+', re.MULTILINE)
    
    headers = pattern.findall(data)
    
        # Find the .fbx file in the input path directory
    for item in os.listdir(output_dir):
        if item.endswith(".fbx"):
            input_base_name = os.path.splitext(item)[0]
            break
    else:
        raise FileNotFoundError("No .fbx file found in the specified directory")

    # Create the directory named ",fbx file named" at the specified output path
    output_dir = os.path.join(output_dir, input_base_name)
    os.makedirs(output_dir, exist_ok=True)
    
    # Define the full path to the output file within the "2line1" directory
    output_file_path = os.path.join(output_dir, "images.txt")
    
    with open(output_file_path, 'w') as file:
        # Writing the specified headers to the output file
        file.write("# Camera pose list data per line\n")
        file.write("# POSE_ID, QW, QX, QY, QZ, TX, TY, TZ, CAMERA_ID\n")
        
        if headers:
            for header in headers:
                file.write(header + '\n')
            print(f"Header information extracted to {output_file_path}")
        else:
            print("No headers found.")
            print("Make sure the input file has the correct format and the regex pattern matches the headers.")

    copy_text_file(input_dir, output_dir)


def copy_text_file(source_dir, dest_dir, file_name="cameras.txt"):
    # Ensure the source file exists
    source_file_path = os.path.join(source_dir, file_name)
    if not os.path.exists(source_file_path):
        raise FileNotFoundError(f"The file {file_name} does not exist in the source directory {source_dir}")
    
    # Ensure the destination directory exists, create it if it doesn't
    os.makedirs(dest_dir, exist_ok=True)
    
    # Define the destination file path
    dest_file_path = os.path.join(dest_dir, file_name)
    
    # Copy the file
    shutil.copy2(source_file_path, dest_file_path)
    
    print(f"File {file_name} copied from {source_dir} to {dest_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract headers from a text file.')
    parser.add_argument('--input', type=str, required=True, help='Path to the input directory')
    parser.add_argument('--output', type=str, required=True, help='Path to the output directory')
    
    args = parser.parse_args()
    
    extract_headers(args.input, args.output)
