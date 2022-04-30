import pandas as pd
import numpy as np
import argparse
from src.utils.main import read_yaml
from sklearn.model_selection import train_test_split
import os





if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument('--config','-c',default='config/config.yaml')

    config_d=args.parse_args()
    dataSource=read_yaml(config_d.config)
    #config_d.config
    source_l=dataSource['data_source']
    
    path_to_ICS=os.path.join('data',dataSource['data']['data_source'])
    path_to_prepared=os.path.join(path_to_ICS,'pepared')
    try: 
        os.makedirs(path_to_prepared)
    except Exception as e:
        print('directory already made')
    train_set=os.path.join(path_to_prepared,'train.csv')
    test_set=os.path.join(path_to_prepared,'test.csv')
    df=pd.read_csv(source_l,delimiter=';')
    # assuming that data is completely clean
    total=df.shape[0]
    
    split_P=read_yaml('params.yaml')
    test_size_sta=int(split_P['data_split']['train']*total)
    try:
        df.iloc[:int(split_P['data_split']['train']*total),:].to_csv(train_set,sep=',',index=False)
        df.iloc[test_size_sta:,:].to_csv(test_set,sep=',',index=False)
    except Exception as e:
        print('file has already been created')
    

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.accumulate(args.integers))
