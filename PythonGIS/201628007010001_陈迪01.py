#coding=utf-8
from  osgeo import gdal
"""（1）给定第2章的文件fdem.tif，
将50~100行和50~100列矩形范围内的DEM切割出来，
并存为新tif文件；
"""
#打开tif文件，读取50-100行的矩形范围DEM
dataset=gdal.Open("fdem.tif")
im_geotrans=dataset.GetGeoTransform()
im_proj=dataset.GetProjection()
im_data=dataset.ReadAsArray(50,50,50,50)
#print im_data.dtype.name
#print im_data.shape
del dataset

#写入为新的tif文件
#判断数据类型
if 'int8' in im_data.dtype.name:
    datatype = gdal.GDT_Byte
elif 'int16' in im_data.dtype.name:
    datatype = gdal.GDT_UInt16
else:
    datatype = gdal.GDT_Float32
#判断数组维数
if len(im_data.shape) == 3:
    im_bands, im_height, im_width = im_data.shape
else:
    im_bands, (im_height, im_width) = 1, im_data.shape
#创建文件
driver=gdal.GetDriverByName("GTiff")
dataset = driver.Create("fdem_new.tif", im_width, im_height, im_bands, datatype)
dataset.SetGeoTransform(im_geotrans) #写入仿射变换参数
dataset.SetProjection(im_proj) #写入投影
#print im_bands
if im_bands == 1:
    dataset.GetRasterBand(1).WriteArray(im_data) #写入数组数据
else:
    for i in range(im_bands):
        dataset.GetRasterBand(i+1).WriteArray(im_data[i])
del dataset




