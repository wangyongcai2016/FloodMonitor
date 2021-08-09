#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Created the fpar/SetNull_batch.py in PyCharm on 十月 17 18:51:11 2018
@author:wangyc
"""
import os
import arcpy
import arcpy.sa
import glob
import fnmatch


def MosaicToNewRaster(inraters,outpath,outraster,proj):
    arcpy.MosaicToNewRaster_management(inraters,outpath,outraster,proj,"8_BIT_UNSIGNED","#","1","LAST","FIRST")

def SetNull(inRaster,whereClause,inFalseRaster,outRaster):
    outSetNull = arcpy.sa.SetNull(inRaster,inFalseRaster,whereClause)
    outSetNull.save(outRaster)

def ExtractRasterByFeature(inraster,infeature,outraster):
    outExtractByMask = arcpy.sa.ExtractByMask(inraster,infeature)
    outExtractByMask.save(outraster)
def clipraster(inraster,outraster,infeature):
    arcpy.Clip_management(inraster, "#", outraster,infeature, "#", "ClippingGeometry")

if __name__ == '__main__':
    inRasterPath = r"I:\GPP_2021\Month\2019"
    infc = r"D:\科研\DHI_2001-2018\Boundary\CHINA_boundary.shp"
    outclip = r'I:\FPAR\FAPAR_500m_year_variable\MEAN\MEAN_Clip'
    outsetnull = r"I:\GPP_2021\Month_SetNull\2019"
    arcpy.env.workspace = inRasterPath
    for f in arcpy.ListRasters("*","TIF"):
        outsetnullfname = os.path.join(outsetnull,f)
        outSetNull = arcpy.sa.SetNull(f, f, "VALUE > 195000")
        #outRas = outSetNull / 10.0
        outSetNull.save(outsetnullfname)

    '''
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = inRasterPath
    arcpy.env.cellSize = 30
    p = Pinyin()
    inRasters = arcpy.ListRasters("*","TIF")
    inFeatures = glob.glob(os.path.join(inFeaturePath,"*.tif"))
    i = 0
    for f in arcpy.ListRasters("*","TIF"):
        filename = str(p.get_pinyin(f))
        for ff in inFeatures:
            inFcfilename = os.path.basename(ff)
            if fnmatch.fnmatch(filename[:10],inFcfilename[:10]):
                outratser = os.path.join(outpath,filename)
                if os.path.exists(outratser):
                    continue
            #加入异常处理机制，防止执行错误导致处理停止
                try:
                    ExtractRasterByFeature(f,ff,outratser)
                except arcpy.ExecuteError as e:
                    print e
                continue

    
    basepath = u'F:/报告/2017年优先区开发建设用地/Zonation/Rank'
    outpath = u'F:/报告/2017年优先区开发建设用地/Zonation/Top20'
    imgfilepath = [os.path.join(basepath,f) for f in os.listdir(basepath)]
    subfilepath = [glob.glob(os.path.join(f,"*rank.compressed.tif")) for f in imgfilepath]
    imfiles = [j for i in subfilepath for j in i]     #列表推导
    for f in imfiles:
        outRaster = os.path.join(outpath,os.path.basename(f).replace(".CAZ_E.rank.compressed",""))
        SetNull(f,"VALUE < 0.8",1,outRaster)
        print "done:{0}".format(outRaster)
    
    basepath = u'G:/DataSet/17年不透水层'
    outpath = u'F:/报告/2017年优先区开发建设用地/building'
    imgfilepath = [os.path.join(os.path.join(basepath,f),u"结果") for f in os.listdir(basepath)]
    subfilepath = [glob.glob(os.path.join(f,"*.tif")) for f in imgfilepath]
    imfiles = [j for i in subfilepath for j in i]     #列表推导
    for f in imfiles:
        outraster = os.path.join(outpath,os.path.basename(f))
        SetNull(f,"VALUE = 0",f,outraster)
        print outraster
    '''