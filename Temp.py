#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Created the Code/Temp.py in PyCharm on 十月 20 23:23:18 2019
@author:wangyc
"""
import numpy as np
import pandas as pd, os
from sklearn.feature_extraction import DictVectorizer

def one_hot_dataframe(data, cols, replace=False):
    vec = DictVectorizer()
    mkdict = lambda row: dict((col, row[col]) for col in cols)
    vecData = pd.DataFrame(vec.fit_transform(data[cols].apply(mkdict, axis=1)).toarray())
    vecData.columns = vec.get_feature_names()
    vecData.index = data.index
    if replace is True:
        data = data.drop(cols, axis=1)
        data = data.join(vecData)
    return data, vecData, vec

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

df = pd.DataFrame(data)

df2, _, _ = one_hot_dataframe(df, ['state'], replace=True)
print(df2)