#coding=utf-8
from osgeo import gdal, ogr, osr
gdal.SetConfigOption("GDAL_DATA", "C:\Program Files (x86)\GDAL\gdal-data")
#定义投影
source = osr.SpatialReference()
source.ImportFromEPSG(4326) #wgs84
target = osr.SpatialReference()
target.ImportFromEPSG(3857) #Google
coordTrans = osr.CoordinateTransformation(source, target)
#投影转换
coordTrans.TransformPoint(117,40) #简单的点转换
coordTrans.TransformPoints([(117,40),(117.5,39.5)]) #点数组转换
g= ogr.CreateGeometryFromWkt("POINT(117 40)") #复杂的 SF 几何对象转换

g.ExportToWkt()
g.GetX(), g.GetY()
print g.Transform(coordTrans)
g.ExportToWkt()
print g.GetX(), g.GetY()