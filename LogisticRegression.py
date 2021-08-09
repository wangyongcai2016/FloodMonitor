#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Created the Code/LogisticRegression.py in PyCharm on 四月 08 10:31:26 2021
@author:wangyc
"""

import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score
import numpy as np
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import seaborn as sns
import scikitplot as skplt
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder





if __name__ == '__main__':
    feat_list = ['DEM','TWI','Hand','STI','SPI','Slope','Aspect','Curve','RiverDis','LULC','SoilType']
    feat_norm = ['DEM','TWI','Hand','STI','SPI','Slope','Aspect','Curve','RiverDis']
    data = pd.read_excel(r"E:\Xuzhihongqu_inunding\Data\LogisticRession\Features_label.xlsx")
    category_field = ['LULC','SoilType']
    dummy_lulc = pd.get_dummies(data['LULC'])
    dummy_lulc[dummy_lulc.columns] = dummy_lulc
    dummy_soiltype = pd.get_dummies(data['SoilType'])
    dummy_soiltype[dummy_soiltype.columns] = dummy_soiltype
    dummy_soiltype = pd.get_dummies(data['SoilType'])
    data = pd.concat([data,dummy_lulc,dummy_soiltype], axis=1)
    data = data.drop(category_field,axis=1)
    x = data.drop(['FID','Id','Y','TRI'],axis=1)
    y = data['Y']
    for feaname in feat_norm:
        x[feaname] = (x[feaname] - x[feaname].mean()) / x[feaname].std()
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=0)
    x_colnum = x_train.columns
    model = LogisticRegression(random_state=0).fit(x_train,y_train)


    y_predict = model.predict(x_test)
    acc_score = accuracy_score(y_test,y_predict)


    prec_score = precision_score(y_test, y_predict)
    re_score = recall_score(y_test, y_predict)
    f1_score = f1_score(y_test, y_predict)
    report = classification_report(y_test,y_predict)

    y_train_probs = model.predict_proba(x_train)
    train_roc_score = roc_auc_score(y_train, y_train_probs[:, 1])

    y_test_probs = model.predict_proba(x_test)
    test_roc_score = roc_auc_score(y_test,y_test_probs[:,1])

    print(acc_score, prec_score, re_score, f1_score)
    print(report)

    print("train auc score:{}".format(train_roc_score))
    print("test auc score:{}".format(test_roc_score))


    #---------------------------train------------------------------
    predictions = cross_val_predict(model, x_train, y_train, cv=3)
    fp_filter = (predictions == 1) & (y_train == 0)
    fp = len(predictions[fp_filter])

    # True positives.
    tp_filter = (predictions == 1) & (y_train == 1)
    tp = len(predictions[tp_filter])

    # False negatives.
    fn_filter = (predictions == 0) & (y_train == 1)
    fn = len(predictions[fn_filter])

    # True negatives
    tn_filter = (predictions == 0) & (y_train == 0)
    tn = len(predictions[tn_filter])

    # Rates
    sst_train = tp / (tp + fn)
    spf_train = tn / (fp + tn)
    ppv_train = tp / (fp + tp)
    npv_train = tp / (tn + fn)

    rates_train = [sst_train,spf_train,ppv_train,npv_train]
    print("rates train:{}".format(rates_train))

    ##------------------------test--------------------------------
    predictions_test = cross_val_predict(model, x_test, y_test, cv=3)
    fp_filter_test = (predictions_test == 1) & (y_test == 0)
    fp_test = len(predictions_test[fp_filter_test])

    # True positives.
    tp_filter_test = (predictions_test == 1) & (y_test == 1)
    tp_test = len(predictions_test[tp_filter_test])

    # False negatives.
    fn_filter_test = (predictions_test == 0) & (y_test == 1)
    fn_test = len(predictions_test[fn_filter_test])

    # True negatives
    tn_filter_test = (predictions_test == 0) & (y_test == 0)
    tn_test = len(predictions_test[tn_filter_test])

    # Rates
    sst_test = tp_test / (tp_test + fn_test)
    spf_test = tn_test / (fp_test + tn_test)
    ppv_test = tp_test / (fp_test + tp_test)
    npv_test = tp_test / (tn_test + fn_test)

    rates_test = [sst_test, spf_test, ppv_test, npv_test]
    print("rates test:{}".format(rates_test))

    #--------------------------plot----------------------------------------------
    #skplt.metrics.plot_roc_curve(y_test,y_probs,curves=('each_class'))
    skplt.metrics.plot_roc_curve(y_test, y_test_probs)
    skplt.metrics.plot_roc_curve(y_train,y_train_probs)

    plt.savefig(r'E:\Xuzhihongqu_inunding\Data\LogisticRession\Roc.jpg')
    plt.show()

    importance = model.coef_[0]
    # summarize feature importance
    for i, v in enumerate(importance):
        print('Feature: %0d, Score: %.5f' % (i, v))
    # plot feature importance
    #plt.bar([x for x in range(len(importance))], [abs(i) for i in importance])
    plt.bar([x for x in x_colnum],[abs(i) for i in importance])
    plt.show()










