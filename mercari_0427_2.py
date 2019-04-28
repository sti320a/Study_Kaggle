from sklearn.model_selection import train_test_split
from sklearn import metrics
from IPython.display import display
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import numpy as np
import pandas as pd
pd.set_option('display.float_format', lambda x: '%.5f' % x)

types_dict_train = {'train_id': 'int64', 'item_condition_id': 'int8',
                    'price': 'float64', 'shipping': 'int8'}
types_dict_test = {'test_id': 'int64',
                   'item_condition_id': 'int8', 'shipping': 'int8'}

train = pd.read_csv('./dataset/train.tsv', delimiter='\t',
                    low_memory=True, dtype=types_dict_train)
test = pd.read_csv('./dataset/test.tsv', delimiter='\t',
                   low_memory=True, dtype=types_dict_test)

print(train.head())
print(test.head())

print(train.shape, test.shape)
