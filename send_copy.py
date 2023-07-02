import os
import subprocess

# Set the serial port
port = "/dev/ttyUSB0"

# Set the path to the source folder
src_folder = "src"

# Check if the root directory already exists on the ESP32
root_exists = subprocess.run(["ampy", "--port", port, "ls", "/"], capture_output=True).returncode == 0

# Create the root directory if it doesn't exist
if not root_exists:
    subprocess.run(["ampy", "--port", port, "mkdir", "/"], check=True)

# Iterate over files and directories in the source folder
for root, dirs, files in os.walk(src_folder):
    # Create the corresponding directory structure on the ESP32
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        target_dir = os.path.join("/", os.path.relpath(dir_path, src_folder))
        subprocess.run(["ampy", "--port", port, "mkdir", target_dir], check=True)
        print(f"Created directory {target_dir}")

# Iterate over files in the source folder and copy them to the ESP32
for root, dirs, files in os.walk(src_folder):
    for file in files:
        src_file = os.path.join(root, file)
        target_file = os.path.join("/", os.path.relpath(src_file, src_folder))
        subprocess.run(["ampy", "--port", port, "put", src_file, target_file], check=True)
        print(f"Copied {src_file} to {target_file}")

