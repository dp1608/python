#!/usr/bin/env python
#coding=utf-8

#import osgeo.gdal as gdal
from osgeo import gdal,osr
import numpy as np

class IMAGE:
    def __init__(self):
        #
        self.colorlist = []
        self.colordict = {}
        fh = open("sng_image.conf")
        lns = [ln.strip() for ln in fh.readlines()]
        fh.close()
        for ln in lns:
            color,rgba = ln.split(":")
            r,g,b,a = [int(v) for v in rgba.split(",")]
            self.colorlist += [color]
            self.colordict[color] = (r,g,b,a)
        #
        #initialize color table
        self.default_ct = None
    #
    def read(self,file):
        dataset=gdal.Open(file)
        im_width = dataset.RasterXSize
        im_height = dataset.RasterYSize
        im_bands = dataset.RasterCount
        im_geotrans = dataset.GetGeoTransform()
        im_proj = dataset.GetProjection()
        print type(im_proj)
        # im_proj = osr.SpatialReference()
        # im_proj.ImportFromEPSG(32650)
        #im_projref = dataset.GetProjectionRef()
        """
        ct = dataset.GetRasterBand(1).GetRasterColorTable()
        if ct is not None:
            for i in range(min(256,ct.GetCount())):
                entry = ct.GetColorEntry(i)
                print i,entry,'read'
            self.default_ct = ct
        """
        #
        #print im_bands,im_width,im_height,im_geotrans
        im_data = np.array(dataset.ReadAsArray(0,0,im_width,im_height))
        #im_data = np.array(dataset.ReadAsArray(0,0,100,50))
        dataset=None
        #
        return (im_data,im_geotrans,im_proj)

    #
    def write(self,file,trans,proj,data):
        #gdal.GDT_Byte, GDT_UInt16, GDAL.GDT_Int16, GDAL.GDT_UInt32, GDAL.GDT_Int32,
        #GDAL.GDT_Float32, GDAL.GDT_Float64
        #print data.dtype.name
        if 'int8' in data.dtype.name:
            datatype = gdal.GDT_Byte
        elif 'int16' in data.dtype.name:
            datatype = gdal.GDT_UInt16
        elif 'int32' in data.dtype.name:
            datatype = gdal.GDT_UInt32
        elif 'float' in data.dtype.name:
            datatype = gdal.GDT_Float32
        else:
            datatype = gdal.GDT_Float32
        #
        if len(data.shape) == 3:
            band,row,col = data.shape
        else:
            band,(row,col) = 1,data.shape
        #
        #print band,row,col,data.dtype.name
        #
        driver = gdal.GetDriverByName("GTiff")
        ds = driver.Create(file,col,row,band,datatype)
        #ds = driver.Create(file,col,row,band,datatype,options=["INTERLEAVE=PIXEL",'TFW=YES','COMPRESS=DEFLATE'])
        #driver = gdal.GetDriverByName("HFA")
        #ds = driver.Create(file,col,row,band,datatype)
        ds.SetGeoTransform(trans)
        ds.SetProjection(proj)
        if band == 1:
            ds.GetRasterBand(1).WriteArray(data)
        else:
            for b in range(band):
                ds.GetRasterBand(b+1).WriteArray(data[b])
        ds = None

    #
    def write_tile(self,file,trans,proj,tiles):
        #gdal.GDT_Byte, GDT_UInt16, GDAL.GDT_Int16, GDAL.GDT_UInt32, GDAL.GDT_Int32,
        #GDAL.GDT_Float32, GDAL.GDT_Float64
        data = tiles[0][0]
        if 'int8' in data.dtype.name:
            datatype = gdal.GDT_Byte
        elif 'int16' in data.dtype.name:
            datatype = gdal.GDT_UInt16
        elif 'int32' in data.dtype.name:
            datatype = gdal.GDT_UInt32
        elif 'float' in data.dtype.name:
            datatype = gdal.GDT_Float32
        else:
            datatype = gdal.GDT_Float32
        #
        if len(data.shape) == 3:
            band,blocksize_y,blocksize_x = data.shape
        else:
            band,(blocksize_y,blocksize_x) = 1,data.shape
        row,col = len(tiles)*blocksize_y,len(tiles[0])*blocksize_x
        #
        print band,row,col,data.dtype.name
        #
        driver = gdal.GetDriverByName("GTiff")
        ds = driver.Create(file,col,row,band,datatype,options=["TILED=YES", "COMPRESS=JPEG", "BLOCKXSIZE=%i" % (blocksize_x), "BLOCKYSIZE=%i" % (blocksize_y)])
        ds.SetGeoTransform(trans)
        ds.SetProjection(proj)
        #
        if band == 1:
            if not self.default_ct is None:
                ds.GetRasterBand(1).SetRasterColorTable(self.default_ct)
                if not self.default_ct is None:
                    #for i in range(min(256,self.default_ct.GetCount())):
                    for i in range(self.default_ct.GetCount()):
                        entry = self.default_ct.GetColorEntry(i)
                        print i,entry,'write_tile'
            for i in range(row/blocksize_y):
                for j in range(col/blocksize_x):
                    ds.GetRasterBand(1).WriteArray(tiles[i][j],j,i)
                    ds.GetRasterBand(1).FlushCache()
        else:
            for b in range(band):
                for i in range(row/blocksize_y):
                    for j in range(col/blocksize_x):
                        #print i,j
                        ds.GetRasterBand(b+1).WriteArray(tiles[i][j][b],j*blocksize_x,i*blocksize_y)
                        ds.GetRasterBand(b+1).FlushCache()
        ds = None

    #
    def write_ic(self,file,trans,proj,data):
        band,(row,col) = 1,data.shape
        #print band,row,col,data.dtype.name

        #tiff driver
        format = "GTiff"
        driver = gdal.GetDriverByName(format)
        metadata = driver.GetMetadata()
        if metadata.has_key(gdal.DCAP_CREATE) and metadata[gdal.DCAP_CREATE] == 'YES':
            pass
            #print 'Driver %s supports Create() method.' % format

        #create new tiff
        dst_ds = driver.Create( file,col,row,1,gdal.GDT_Byte)
        #dst_ds.SetColorInterpretation(2)
        dst_ds.GetRasterBand(1).SetRasterColorTable( self.ct )
        #dst_ds.SetMetadata()
        dst_ds.SetGeoTransform(trans)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(data)
        #close new tiff
        dst_ds.GetRasterBand(1).FlushCache()
        ds = None
        #del dst_ds

#
if __name__ == "__main__":
    inputfile = 'fdem.tif'
    outputfile = 'fdem30ff.tif'
    test = IMAGE()
    im_data,im_geotrans,im_proj = test.read(inputfile)
    test.write(outputfile,im_geotrans,im_proj,im_data)
