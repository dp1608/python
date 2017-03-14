#coding=utf-8
from osgeo import ogr, gdal, osr
import os

gdal.SetConfigOption('GDAL_FILENAME_IS_UTF8', 'NO') # 解决中文路径
gdal.SetConfigOption("GDAL_DATA", "C:\Program Files (x86)\GDAL\gdal-data")
#gdal.SetConfigOption('SHAPE_ENCODING', 'gb2312') # 解决 SHAPE 文件的属性值

filename = "pnt_new.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
if os.access(filename, os.F_OK ): #如文件已存在，则删除
    driver.DeleteDataSource(filename)

ds = driver.CreateDataSource(filename) #创建shape文件

spatialref = osr.SpatialReference() #创建一个空的空间参考
spatialref.ImportFromEPSG(4326) #WGS84地理坐标系

geomtype = ogr.wkbPoint
layer = ds.CreateLayer(filename [:-4], srs=spatialref, geom_type=geomtype) #创建图层

fd1 = ogr.FieldDefn('pname',ogr.OFTString)
fd2 = ogr.FieldDefn('pid',ogr.OFTInteger)
layer.CreateField(fd1)
layer.CreateField(fd2)

geom=ogr.CreateGeometryFromWkt('POINT(117 40)')
feat = ogr.Feature(layer.GetLayerDefn()) #创建 SF
feat.SetGeometry(geom)
feat.SetField('pname', 'song')
feat.SetField('pid', 11)
layer.CreateFeature(feat)

