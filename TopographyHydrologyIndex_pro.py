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
    DEM_filled = Fill(inDEM)    #Fill DEM
    outFlowDirection = FlowDirection(DEM_filled, "FORCE")   #flow direction
    outFlowAccumulation = FlowAccumulation(outFlowDirection, "", "FLOAT") + 1 # flow accumulation
    slope_radians = Slope(DEM_filled,"DEGREE","")    #slope
    #slope_radians = slope * math.pi / 180.0    # slope degree to radius
    TWI = Ln(outFlowAccumulation / (Tan(slope_radians) + .01))   #calculate 
    SPI = Ln(outFlowAccumulation * Tan(slope_radians))
    STI = Power(outFlowAccumulation/22.13,0.6) * Power(Sin(slope_radians/0.0896),1.3)
    DEM_min = FocalStatistics(DEM_filled, NbrRectangle(3,3,"CELL"),"MINIMUM","NODATA")
    DEM_max = FocalStatistics(DEM_filled, NbrRectangle(3,3,"CELL"),"MAXIMUM","NODATA")
    TRI = SquareRoot(Abs(Square(DEM_max) - Square(DEM_min)))
    return DEM_filled,outFlowDirection,outFlowAccumulation,slope_radians,TWI,SPI,STI,TRI

if __name__ == '__main__':
    inpath = r"F:\SRTM\unzip"
    outpath = r"F:\SRTM\var_degree"
    arcpy.env.overwriteOutput = True
    for f in glob.glob(os.path.join(inpath,"*.hgt")):
        fname = os.path.basename(f)
        fill_fname = os.path.join(outpath,os.path.splitext(fname)[0] + "_FILL.tif")
        fd_fname = os.path.join(outpath,os.path.splitext(fname)[0] + "_FD.tif")
        fa_fname = os.path.join(outpath,os.path.splitext(fname)[0] + "_FA.tif")
        slope_fname = os.path.join(outpath,os.path.splitext(fname)[0] + "_SlopeR.tif")
        twi_fname = os.path.join(outpath,os.path.splitext(fname)[0] + "_TWI.tif")
        spi_fname = os.path.join(outpath, os.path.splitext(fname)[0] + "_SPI.tif")
        sti_fname = os.path.join(outpath, os.path.splitext(fname)[0] + "_STI.tif")
        tri_fname = os.path.join(outpath, os.path.splitext(fname)[0] + "_TRI.tif")
        FILL,FD,FA,SLOPEr,TWI,SPI,STI,TRI = HydroIndex(f)
        FILL.save(fill_fname)
        FD.save(fd_fname)
        FA.save(fa_fname)
        SLOPEr.save(slope_fname)
        TWI.save(twi_fname)
        SPI.save(spi_fname)
        STI.save(sti_fname)
        TRI.save(tri_fname)