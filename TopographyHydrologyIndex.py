#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Created the Code/TopographyHydrologyIndex.py in PyCharm on 十月 06 21:51:40 2020
@author:wangyc
"""
import os
import glob
import arcpy
from arcpy.sa import *
import math

def HydroIndex(inDEM):
    DEM_filled = arcpy.sa.Fill(inDEM)    #Fill DEM
    outFlowDirection = arcpy.sa.FlowDirection(DEM_filled, "NORMAL","","D8")   #flow direction
    outFlowAccumulation = arcpy.sa.FlowAccumulation(outFlowDirection, "", "FLOAT") + 1   # flow accumulation
    slope = arcpy.sa.Slope(DEM_filled,"DEGREE","","PLANAR")    #slope
    slope_radians = slope * math.pi / 180.0
    TWI = arcpy.sa.Ln(outFlowAccumulation / (arcpy.sa.Tan(slope_radians) + .01))
    SPI = outFlowAccumulation * arcpy.sa.Tan(slope_radians)
    STI = arcpy.sa.Power(outFlowAccumulation/22.13,0.6) * arcpy.sa.Power(arcpy.sa.Sin(slope_radians/0.0896),1.3)
    #DEM_min = arcpy.sa.FocalStatistics(DEM_filled, NbrRectangle(3,3,"MAP"),"MINIMUM","")
    #DEM_max = arcpy.sa.FocalStatistics(DEM_filled,NbrRectangle(3,3,"MAP"),"MAXIMUM","")
    #TRI = arcpy.sa.SquareRoot(arcpy.sa.Abs(arcpy.sa.Square(DEM_max) - arcpy.sa.Square(DEM_min)))
    return TWI,SPI,STI

if __name__ == '__main__':
    inpath = r"F:\SRTM\unzip"
    outpath = r"F:\SRTM\Hyd_var"
    for f in glob.glob(os.path.join(inpath,"*.hgt")):
        fname = os.path.basename(f)
        twi_fname = os.path.join(outpath,os.path.splitext(fname)[0] + "_TWI.tif")
        spi_fname = os.path.join(outpath, os.path.splitext(fname)[0] + "_SPI.tif")
        sti_fname = os.path.join(outpath, os.path.splitext(fname)[0] + "_STI.tif")
        tri_fname = os.path.join(outpath, os.path.splitext(fname)[0] + "_TRI.tif")
        TWI,SPI,STI = HydroIndex(f)
        TWI.save(twi_fname)
        SPI.save(spi_fname)
        STI.save(sti_fname)
        #TRI.save(tri_fname)