#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Created the Code/VIF.py in PyCharm on 四月 25 15:36:06 2021
@author:wangyc
"""

import os
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd


def calc_vif(X):
    # Calculating VIF
    vif = pd.DataFrame()
    vif["variables"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif

if __name__ == '__main__':
    data = pd.read_excel(r"E:\Xuzhihongqu_inunding\Data\LogisticRession\Features_label.xlsx")
    data = data.drop(["FID","Id","Y"],axis = 1)
    lulc_unique = data["LULC"].unique().tolist()
    soiltype_unique = data["SoilType"].unique().tolist()


    for i,l in enumerate(lulc_unique):
        data.loc[data["LULC"] == l,"LULC"] = i

    for j,s in enumerate(soiltype_unique):
        data.loc[data["SoilType"] == s,"SoilType"] = j

    data = data.drop("TRI",axis=1)
    vif = calc_vif(data)


