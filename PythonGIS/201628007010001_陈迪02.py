#coding=utf-8
"""（2）编写一个小程序，其中，
自定义一个类（如：GRID），
至少包括三个函数read、clip、write，
分别用于读栅格文件、切片、和写结果文件；"""

import os,sys
from osgeo import gdal

class Grid():
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        self.dataset=gdal.Open(self.filename)
        self.im_geotrans = self.dataset.GetGeoTransform()
        self.im_proj = self.dataset.GetProjection()
        return  self.dataset

    def clip(self,xoff=0,yoff=0,width=None,length=None):
        self.im_data = self.dataset.ReadAsArray(xoff, yoff, width, length)
        return self.im_data

    def write(self,outputfile):
        datatype = gdal.GDT_UInt16
        # 判断数组维数
        if len(self.im_data.shape) == 3:
            im_bands, im_height, im_width = self.im_data.shape
        else:
            im_bands, (im_height, im_width) = 1, self.im_data.shape
        driver = gdal.GetDriverByName("GTiff")
        dataset = driver.Create(outputfile, im_width, im_height, im_bands, datatype)
        dataset.SetGeoTransform(self.im_geotrans)  # 写入仿射变换参数
        dataset.SetProjection(self.im_proj)  # 写入投影
        return outputfile

Picture=Grid('fdem.tif')
Picture.read()
Picture.clip(50,50,100,100)
Picture.write("testnew.tif")



