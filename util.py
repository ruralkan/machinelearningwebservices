# To obtain train data file 
# https://www.kaggle.com/c/digit-recognizer/data

import numpy as np
import pandas as pd

def get_data(limit=None):
    print("Reading in and transforming data...")
    df = pd.read_csv('./large_files/train.csv')
    data = df.values
    np.random.shuffle(data)
    X = data[:, 1:] / 255.0 # data is from 0..255
    Y = data[:, 0]
    if limit is not None:
        X, Y = X[:limit], Y[:limit]
    return X, Y
