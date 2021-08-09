#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Created the Code/ImportancePlot.py in PyCharm on 四月 23 08:51:16 2021
@author:wangyc
"""
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_feature_importance(importance,names):
    feature_importance = np.array(importance)
    feature_names = np.array(names)
    data = {"feature_names":feature_names,"feature_importance":feature_importance}
    fi_df = pd.DataFrame(data)
    # Sort the DataFrame in order decreasing feature importance
    fi_df.sort_values(by=['feature_importance'], ascending=False, inplace=True)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    sns.set(font='SimHei')  # 解决Seaborn中文显示问题
    # Define size of bar plot
    plt.figure(figsize=(10, 8))
    # Plot Searborn bar chart
    sns.barplot(x=fi_df['feature_importance'], y=fi_df['feature_names'])
    # Add chart labels
    plt.title('FEATURE IMPORTANCE')
    plt.xlabel('FEATURE IMPORTANCE')
    plt.ylabel('FEATURE NAMES')

if __name__ == '__main__':
    data = pd.read_excel(r"E:\Xuzhihongqu_inunding\Data\LogisticRession\coef.xlsx",sheet_name=2)
    #data = data.drop("importance",axis = 1)
    data.sort_values(by = ["importance"],ascending = False,inplace = True)

    #plt.rcParams['font.sans-serif'] = ['simsun']  # 解决中文显示问题-设置字体为黑体
    #plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    plt.figure(figsize = (10,6))
    sns.barplot(x = data["importance"],y = data["variable"])
    #plt.title(u"Logistics Regression Feature Importance")
    #plt.xlabel(u"Feature Importance")
    #plt.ylabel(u"Feature Name")

    plt.yticks(fontproperties='Times New Roman', size=14)
    plt.xticks(fontproperties='Times New Roman', size=14)
    #plt.title("特征重要性")
    plt.xlabel("重要性",fontdict={'family': 'simsun', 'size': 16})
    plt.ylabel("变量",fontdict={'family': 'simsun', 'size': 16})

    plt.savefig(r"E:\Xuzhihongqu_inunding\Data\LogisticRession\FeatureImportance_Chinese_new.jpg")
    plt.show()