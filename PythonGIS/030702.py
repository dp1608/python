#coding=utf-8
from osgeo import gdal, ogr, osr
#定义投影
sr = osr.SpatialReference('LOCAL_CS["arbitrary"]' )
#在内存中，创建一个 Shape 文件的图层，含有一个多边形和一条线
source_ds = ogr.GetDriverByName('Memory').CreateDataSource( 'wrk' )
mem_lyr = source_ds.CreateLayer( 'poly', srs=sr ,geom_type=ogr.wkbPolygon )
mem_lyr.CreateField(ogr.FieldDefn('TCODE',ogr.OFTReal))

wkt_geom = ['POLYGON((1020 1030 40,1020 1045 30,1050 1045 20,1050 1030 35,1020 1030 40))',
            'POLYGON((1010 1046 85,1015 1055 35,1055 1060 26,1054 1048 35,1010 1046 85))']
celsius_field_values = [50,200,60]



for i in range(len(wkt_geom)):
    feat = ogr.Feature(mem_lyr.GetLayerDefn() )
    feat.SetGeometryDirectly( ogr.Geometry(wkt = wkt_geom[i]) )
    feat.SetField( 'CELSIUS', celsius_field_values[i] )
    mem_lyr.CreateFeature( feat )

###在内存中，创建一个 100*100 大小的 3 波段的空白图像
target_ds = gdal.GetDriverByName('MEM').Create('', 100, 100, 1, gdal.GDT_Byte )
target_ds.SetGeoTransform( (1000,1,0,1100,0,-1) )
target_ds.SetProjection( sr.ExportToWkt())
#调用栅格化函数
err = gdal.RasterizeLayer( target_ds, [1], mem_lyr, options= ["ATTRIBUTE=TCODE"])
#将内存中的图像，存储到硬
gdal.GetDriverByName('GTiff').CreateCopy('rasterized_poly.tif', target_ds)
del target_ds
del source_ds
