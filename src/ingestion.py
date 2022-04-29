import os
from src.utils.main import read_yaml
from src.utils.main import make_dirs
import pandas as pd
import argparse
def get_data_tolocal(yamlpathconfig):
    config_d=read_yaml(yamlpathconfig)
    raw_source=config_d['data_source']
    print(raw_source)
    root_source=config_d['data']['data_source']
    raw_dir=config_d['data']['raw_folder']
    raw_directory=os.path.join('data',root_source)
    print(raw_dir)
    raw_folder_from_ics=os.path.join(raw_directory,raw_dir)
    make_dirs([raw_folder_from_ics])
    file_source=os.path.join(raw_folder_from_ics,'redwine.csv')
    df=pd.read_csv(raw_source,delimiter=';')
    df.to_csv(file_source,sep=',',index=False)

    







if (__name__)=='__main__':
    args=argparse.ArgumentParser().add_argument('--config','-c',default='config/config.yaml')
    get_data_tolocal(args.default)