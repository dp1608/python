#coding=utf-8
# from  osgeo import gdal
# import  numpy as np
#
# dataset=gdal.Open("fdem.tif") #打开文件
# im_width=dataset.RasterXSize
# im_height=dataset.RasterYSize
# im_bands=dataset.RasterCount
# im_geotrans=dataset.GetGeoTransform()
# im_proj=dataset.GetProjection()
# im_data=dataset.ReadAsArray(0,0,im_width,im_height) #实际上是一个对象，还有一些处理对象的方法
# del dataset
# print  im_data.shape
# print im_data[50:53,14:17]
# print im_data.dtype
#
# datatype=gdal.GDT_UInt16
# driver=gdal.GetDriverByName("GTiff")
# dataset = driver.Create("fdem_new.tif", im_width, im_height, im_bands, datatype)
# dataset.SetGeoTransform(im_geotrans) #写入仿射变换参数
# dataset.SetProjection(im_proj) #写入投影
#
# layer01=dataset.GetRasterBand(1)
# layer01.WriteArray(im_data)
# del dataset

#矢量
from  osgeo import ogr
#WKT Well Known Text
pnt_wkt="POINT(1,1)"
lin_wkt="LINSTRING(0 0,15 15)"
pol_wkt="POLYGON((1 1,1 10,10 10,10 1,1 1),( 2 2,2 8,8 8,8 2,2 2))"

#创建 SF 对象
pnt = ogr.CreateGeometryFromWkt(pnt_wkt)
lin = ogr.CreateGeometryFromWkt(lin_wkt)
pol = ogr.CreateGeometryFromWkt(pol_wkt)

