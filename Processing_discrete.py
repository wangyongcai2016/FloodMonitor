#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Created the Code/Processing_discrete.py in PyCharm on 四月 12 17:25:22 2021
@author:wangyc
"""
import os
import arcpy
import numpy as np
from osgeo import gdal

def write_geotiff(data,fname,cols,rows,bandnum,geotransform,projection):
    driver = gdal.GetDriverByName("GTiff")
    outraster = driver.Create(fname,cols,rows,bandnum,gdal.GDT_Int16)
    outraster.SetProjection(projection)
    outraster.SetGeoTransform(geotransform)
    outband = outraster.GetRasterBand(1)
    #outband.SetNoDataValue(nodata)
    outband.WriteArray(data)

def landcover_dummy(inpath,landcover):
    ds = gdal.Open(landcover)
    cols = ds.RasterXSize
    rows = ds.RasterYSize
    band = ds.GetRasterBand(1)
    #nodata = band.GetNoDataValue()
    projection = ds.GetProjection()
    geotransform = ds.GetGeoTransform()
    data = band.ReadAsArray()

    #data = arcpy.RasterToNumPyArray(landcover)
    shape = data.shape
    forest = np.zeros(shape)
    shrub = np.zeros(shape)
    farmland = np.zeros(shape)
    grassland = np.zeros(shape)
    wetland = np.zeros(shape)
    water = np.zeros(shape)
    impervious = np.zeros(shape)
    bareland = np.zeros(shape)

    forest[np.where(data == 20)] = 1
    farmland[np.where(data == 10)] = 1
    shrub[np.where(data == 40)] = 1
    grassland[np.where(data == 30)] = 1
    wetland[np.where(data == 50)] = 1
    water[np.where(data == 60)] = 1
    impervious[np.where(data == 80)] = 1
    bareland[np.where(data == 90)] = 1

    fnamelist = ["forest","farmland","shrub",
                 "grassland","wetland","water",
                 "impervious","bareland"]
    datalist = [forest,farmland,shrub,
                grassland,wetland,water,
                impervious,bareland]

    data_dict = dict(zip(fnamelist,datalist))

    for key,value in data_dict.items():
        #value[np.where(data == nodata)] = nodata
        write_geotiff(value,os.path.join(inpath,key + "_.tif"),
                      cols,rows,1,geotransform,projection)
        '''
        subras = arcpy.NumPyArrayToRaster(value,
                                          arcpy.Point(minx, miny),
                                          raster.meanCellWidth,
                                          raster.meanCellHeight)
        subras.save(os.path.join(inpath,key + ".tif"))
        
        '''
    return
def soiltype_dummy(inpath,soiltype):

    ds = gdal.Open(soiltype)
    cols = ds.RasterXSize
    rows = ds.RasterYSize
    band = ds.GetRasterBand(1)
    #nodata = band.GetNoDataValue()
    projection = ds.GetProjection()
    geotransform = ds.GetGeoTransform()
    data = band.ReadAsArray()
    shape = data.shape

    YellowCinnamon = np.zeros(shape)
    NewSoil = np.zeros(shape)
    LimeSoil = np.zeros(shape)
    PurpleSoil = np.zeros(shape)
    ChaoSoil = np.zeros(shape)
    SwampSoil = np.zeros(shape)
    PaddySoil = np.zeros(shape)
    RedSoil = np.zeros(shape)
    Urband = np.zeros(shape)
    Lake = np.zeros(shape)
    River = np.zeros(shape)
    SandBar = np.zeros(shape)

    YellowCinnamon[np.where(data == 2)] = 1
    NewSoil[np.where(data == 4)] = 1
    LimeSoil[np.where(data == 5)] = 1
    PurpleSoil[np.where(data == 6)] =1
    ChaoSoil[np.where(data == 10)] = 1
    SwampSoil[np.where(data == 11)] = 1
    PaddySoil[np.where(data == 12)] = 1
    RedSoil[np.where(data == 13)] = 1
    Urband[np.where(data == 15)] = 1
    Lake[np.where(data == 16)] = 1
    River[np.where(data == 17)] = 1
    SandBar[np.where(data == 18)] = 1

    fnamelist = ["YellowCinnamon", "NewSoil", "LimeSoil",
                 "PurpleSoil", "ChaoSoil", "SwampSoil",
                 "PaddySoil", "RedSoil","Urband",
                 "Lake","River","SandBar"]
    datalist = [YellowCinnamon, NewSoil, LimeSoil,
                PurpleSoil, ChaoSoil, SwampSoil,
                PaddySoil, RedSoil, Urband,
                Lake, River, SandBar]
    data_dict = dict(zip(fnamelist,datalist))

    for key,value in data_dict.items():
        #value[np.where(data == nodata)] = nodata
        write_geotiff(value,os.path.join(inpath,key + ".tif"),
                      cols,rows,1,geotransform,projection)

    '''
    for k,v in data_dict.items():
        v[np.where(data == nodata)] = nodata
        subras = arcpy.NumPyArrayToRaster(v,
                                          arcpy.Point(minx, miny),
                                          soilras.meanCellWidth,
                                          soilras.meanCellHeight)
        subras.save(os.path.join(inpath, k + ".tif"))
    '''
    return
if __name__ == '__main__':
    inpath = r"E:\Xuzhihongqu_inunding\Data\SoilType"
    inras = os.path.join(inpath,"研究区SoilType30m_reclass.tif")
    soiltype_dummy(inpath,inras)



