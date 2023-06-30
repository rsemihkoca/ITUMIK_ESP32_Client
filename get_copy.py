import subprocess
import os

def clean_path(path):
    return os.path.normpath(path).replace("\\","/")

def get_file(port, remote_file, local_file):
    command = f'ampy --port {port} get "{clean_path(remote_file)}" "{clean_path(local_file)}"'


    process = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    _, stderr = process.communicate()
    if process.returncode != 0:
        # If an error occurred, treat this as a directory

        return False
    print(f'Saved file: {local_file}')
    return True

def get_files_in_directory(port, directory, local_dir=""):
    command = f'ampy --port {port} ls "{clean_path(directory)}"'


    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    while True:
        line = process.stdout.readline()
        if not line:
            break
        line = line.decode('utf-8').rstrip() # decode byte string to normal string and remove newlines
        remote_path = os.path.join(directory, line)
        local_path = os.path.join(local_dir, line)
        local_file = os.path.join(os.getcwd(), './src' + local_path)
        
        if not os.path.exists(os.path.dirname(local_file)):
            os.makedirs(os.path.dirname(local_file))
        
        # Try to get the file
        if not get_file(port, remote_path, local_file):
            # If there is stderr, it's probably a directory
            # recursively get files in this directory
            get_files_in_directory(port, remote_path, local_path)

port = "/dev/ttyUSB0"
get_files_in_directory(port, "/")
