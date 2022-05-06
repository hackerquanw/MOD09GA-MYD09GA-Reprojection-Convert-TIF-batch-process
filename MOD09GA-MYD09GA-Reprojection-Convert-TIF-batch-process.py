    from osgeo import gdal, osr
    from osgeo import gdal_array
    import os
    import time
    import numpy as np    
    start = time.time() 
    def readHdfWithGeo(hdfFloder, saveFloder):
        #获取输入文件夹中所有的文件名
        hdfNameList = os.listdir(hdfFloder)
        #遍历文件名列表中所有文件
        for i in range(len(hdfNameList)):
            #获取文件名后缀
            dirname, basename = os.path.split(hdfNameList[i])
            filename, txt = os.path.splitext(basename)
            #判断文件后缀是否为 .hdf
            if txt == '.hdf':
                hdfPath = hdfFloder + os.sep + hdfNameList[i]
                #打开hdf文件
                datasets = gdal.Open(hdfPath)
                #打开子数据集
                dsSubDatasets = datasets.GetSubDatasets()
                #打开栅格数据，子集的[0][0]可以改成[1][0]选择另一个子集-每个子集是什么波段要在OSgeo4W下面用info查询，也可以改成for循环，遍历需要的子集。
                for x in range(11,18): #例如遍历提取11-17子集输入11,18
                    someRaster = gdal.Open(dsSubDatasets[x][0])
                    #获取元数据
                    metaData = datasets.GetMetadata()
                    #for key, value in metaData.items():
                    #   print('{key}:{value}'.format(key = key, value = value))
                    #获取数据时间
                    data = metaData['RANGEBEGINNINGDATE']
                    timeOrigin = metaData['LOCALGRANULEID']
                    time = timeOrigin.split(".")[0]+"-"+timeOrigin.split(".")[1]+"-"+timeOrigin.split(".")[2]
                    #命名输出完整路径文件名-文件名就是日期，如果要提取各个不同波段，在.tif之前加上波段号更好
                    outName = saveFloder + os.sep + data + time + '-Dataset-' + str(x) + '.tif' #使用str(x)将x设置为字符串，输出的文件名有子集编号
                    #进行几何校正，这里的someRaster要和前面的一致
                    geoData = gdal.Warp(outName, someRaster,
                                    dstSRS = 'EPSG:4326', format = 'GTiff',
                                    resampleAlg = gdal.GRA_Bilinear) #投影EPSG:32648
                    del geoData
                    print('{outname} deal end'.format(outname = outName))
    start = time.time()      
        # 下面分别是输入、输出路径        
    readHdfWithGeo(r'D:\3Sproject\3Sdata\MODIS\MOD09GA/', 
                   r'D:\3Sproject\3Sdata\MODIS\MOD09GA/')
    end = time.time()
    print('deal spend: {s} s'.format(s = end-start))