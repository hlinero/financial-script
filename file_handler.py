import os.path

def is_config_file_present():
    return os.path.isfile("config.yaml")

def is_file(file_path):
    return os.path.isfile(file_path)