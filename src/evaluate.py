# import necessary libraries
from sklearn.metrics import mean_squared_error
import pickle
import argparse
from src.utils.main import read_yaml
import pandas as pd
import os

# pickle is a dependency
# the read_yaml is a dependency
LR=pickle.load(open('pickle/LRTrained.pkl','rb'))
# the test set is also a dependency
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--config','-c',default='config/config.yaml')
    args=parser.parse_args()
    config_d=read_yaml(args.config)
    root_source=config_d['data']['data_source']
    raw_dir=config_d['data']['raw_folder']
    test=os.path.join('data',root_source,config_d['data']['split_data'],config_d['data']['test'])
    df=pd.read_csv(test)
    dk=mean_squared_error(df.quality,LR.predict(df.drop('quality',axis=1)))
    with open('results.txt','w') as f:
        f.write(str(dk))
