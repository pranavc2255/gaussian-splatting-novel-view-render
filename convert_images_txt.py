import re
import argparse

def extract_headers(input_file, output_file):
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    
    with open(input_file, 'r') as file:
        data = file.read()

    # Regular expression to match the header information for each image
    pattern = re.compile(r'(\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s+\d+)\s+IMG_\d+\.\w+', re.MULTILINE)
    
    headers = pattern.findall(data)
    
    with open(output_file, 'w') as file:
        # Writing the specified headers to the output file
        file.write("# Camera pose list data per line\n")
        file.write("# POSE_ID, QW, QX, QY, QZ, TX, TY, TZ, CAMERA_ID\n")
        
        if headers:
            for header in headers:
                file.write(header + '\n')
            print(f"Header information extracted to {output_file}")
        else:
            print("No headers found.")
            print("Make sure the input file has the correct format and the regex pattern matches the headers.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract headers from a text file.')
    parser.add_argument('--input', type=str, required=True, help='Path to the input file')
    parser.add_argument('--output', type=str, required=True, help='Path to the output file')
    
    args = parser.parse_args()
    
    extract_headers(args.input, args.output)
