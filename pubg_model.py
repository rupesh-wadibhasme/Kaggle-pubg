import numpy as np
import pandas as pd
import sys
sys.path.append('..')

train = pd.read_csv('data/train_V2.csv')

test= pd.read_csv('data/test_V2.csv')

target=train['winPlacePerc']

train=train[0:1000,:]

train.drop(['Id','groupId','matchId','winPlacePerc'],inplace=True)

test.drop(['Id','groupId','matchId'],inplace=True)

combine= pd.concat([train,test],axis=0)


for cols in combine.columns():

