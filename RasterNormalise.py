#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Created the Code/RasterNormalise.py in PyCharm on 四月 17 16:52:20 2021
@author:wangyc
"""

import arcpy
import os

if __name__ == '__main__':
    inpath = r"E:\Xuzhihongqu_inunding\Data\研究区地形变量"
    arcpy.env.workspace = inpath
    for f in arcpy.ListRasters("","TIF"):
        data = arcpy.RasterToNumPyArray(f)
        mean = data.mean()
        std = data.std()
        print(f,mean,std)