# -*- coding: utf-8 -*-
# @StartTime : 2017/4/13 16:17
# @EndTime   : 2017/4/15 13:30
# @Author    : Andy
# @File      : Qizhong0413.py
# @Software  : PyCharm
# 1. 请写一个程序，利用第二章的stations.shp点文件生成一个TIN三角网，并存为Shape文件。目的：巩固OGR矢量文件读写知识，自学scipy.spatial模块的Delaunay类。
# 提交要求：Python源码、Matplotlib生成的结果图片。


from osgeo import ogr
from osgeo import gdal
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import os
from gwp_shape import SHAPE

# 读取文件

# 为了支持中文路径，请添加下面这句代码
gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
# 为了使属性表字段支持中文，请添加下面这句
gdal.SetConfigOption("SHAPE_ENCODING", "")
# 注册所有的驱动
ogr.RegisterAll()

filename="stations.shp"
ds=ogr.Open(filename,False)
layer=ds.GetLayer(0)

spatialref=layer.GetSpatialRef()
# print spatialref
lydefn=layer.GetLayerDefn()
geomtype=lydefn.GetGeomType()
# print geomtype

fieldlist = [] #字段列表 （字段类型，OFTInteger, OFTReal, OFTString, OFTDateTime）
for i in range(lydefn.GetFieldCount()):
    fddefn = lydefn.GetFieldDefn(i)
    fddict = {'name':fddefn.GetName(),'type':fddefn.GetType(),
            'width':fddefn.GetWidth(),'decimal':fddefn.GetPrecision()}
    fieldlist += [fddict]
# print fieldlist

geomlist, reclist = [], [] #SF 数据记录 – 几何对象及其对应属性
feature = layer.GetNextFeature() #获得第一个 SF
while feature is not None:
    geom = feature.GetGeometryRef()
    geomlist += [geom.ExportToWkt()]
    rec = {}
    for fd in fieldlist:
        rec[fd['name']] = feature.GetField(fd['name'])
    reclist += [rec]
    feature = layer.GetNextFeature()
# print geomlist
# print "cut"
# print reclist

points = np.zeros((len(geomlist),2),dtype=np.float)
for i in range(len(reclist)): #将 SF 数据记录（几何对象及其属性写入图层）
    geom = ogr.CreateGeometryFromWkt(geomlist[i])
    points[i,0],points[i,1] = geom.GetX(),geom.GetY()
ds.Destroy()
# print points.shape

# 生成TIN

tri = Delaunay(points)
delaunay=tri.simplices.copy()            #各三角形索引 0-174

plt.triplot(points[:, 0], points[:, 1], tri.simplices.copy())  # 绘制三角格网
plt.plot(points[:, 0], points[:, 1], 'o')  # 绘制这些离散点
plt.xlim(00000, 1000000)
plt.ylim(00000, 1000000)
plt.show()


# 写入points,形式Polygon
outputfile="TIN_stations.shp"
shape_driver=SHAPE()
geomtypeo=ogr.wkbPolygon
fieldlisto_ = [{'width': 20, 'decimal': 0, 'type': ogr.OFTInteger, 'name': 'ID'},
                {'width': 20, 'decimal': 3, 'type': ogr.OFTReal, 'name': 'AREA'},
                {'width': 20, 'decimal': 3, 'type': ogr.OFTReal, 'name': 'ANN_PREC'}
            ]
geomlist_,reclist_=[],[]
# print 'cut3'
for i in range(len(delaunay)):
    if len(delaunay[i])==0:
        continue
    if -1 in delaunay[i]:
        continue
    coords=[]
    for j in delaunay[i]:
        x,y=points[j,0],points[j,1]
        coords.append("%f %f"%(x,y))
    coords.append("%f %f"%(points[delaunay[i][0],0],points[delaunay[i][0],1]))
    wkt_ = "POLYGON ((%s))"%(','.join(coords))
    rec_={}
    rec_['ID']=i
    rec_['AREA']=ogr.CreateGeometryFromWkt(wkt_).GetArea()
    rec_['ANN_PREC']=0.0
    geomlist_.append(wkt_)
    reclist_.append(rec_)
# print reclist_
# print geomlist_
shape_driver.write_shp(outputfile,spatialref,geomtypeo,geomlist_,fieldlisto_,reclist_)
