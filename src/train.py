from sklearn.linear_model import LinearRegression
from src.utils.main import read_yaml
import pandas as pd
import os
import pickle

import argparse
lr=LinearRegression()

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--config','-c',default='config/config.yaml')
    args=parser.parse_args()
    config_d=read_yaml(args.config)
    root_source=config_d['data']['data_source']
    raw_dir=config_d['data']['raw_folder']
    train=os.path.join('data',root_source,config_d['data']['split_data'],config_d['data']['train'])
    df=pd.read_csv(train)
    trained=lr.fit(X=df.drop('quality',axis=1),y=df.quality)
    pickle.dump(trained,open('pickle/LRTrained.pkl','wb'))
    #print(trained.coef_)
    # everytime you go to fetch data always go through yaml


    
