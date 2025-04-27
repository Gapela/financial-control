import pandas as pd
from configparser import ConfigParser as cf
import os

def config_parser(path):
    """
    Return a method to acess all values contained in .config file.

    Params:
    - Path =  path of .config file

    Example:
    You can use like this: 
        var = config_parser()
        var['DIR_PATHS']['files']

    It'll return the path as value contained in 'files', under 'Path'.
    """
    try:
        config = cf()
        if not os.path.exists(path):
            raise FileNotFoundError(f"The '{path}' file does not exist.")
        config.read(path)
        if not config.sections():
            raise ValueError(f"The '{path}' file is empty or improperly formatted.")
        return config
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def list_dir_files(path):
    """
    This function create a list of all files contained in a directory.
    
    Params:
        - path = Directory path.
    """
    try:
        list_files = os.listdir(path)
        print(list_files)
        return list_files
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return []
    

# cf = config_parser('.config')
# files_path = cf['DIR_PATHS']['files']
# files_list = list_dir_files(files_path)

# print('files_path: ', files_path)
# print('files_list: ', files_list)