import pandas as pd
from os_managment import config_parser, list_dir_files

def read_csv(path):
    """
    Read a csv file from a path.

    Params:
    - path = path of the file wanted.
    """
    try:
        data = pd.read_csv(path)
        return data
    except Exception as e:
        print("Error:", e)


def concat_csv(list_fileDir):
    """
    From a list of csv's files, make a big one csv.

    Params:
    - list_fileDir = a list of csv's path that you want to concatenate.
    """
    pass

def csv_to_df(csv_path):
    """
    Make a DataFrames using Pandas lib from a csv input.

    Params:
    - csv_path = Directorys' csv that you want to convert into a DF
    """
    pass