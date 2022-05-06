# MOD09GA-MYD09GA-Reprojection-Convert-TIF-batch-process
# programming language: python
# introduction 介绍
- MODIS反射率产品是计算地球地表反照率过程中最常用的数据，分为MOD09GA与MYD09GA两种，分别对应terra与aqua卫星。MOD09GA/MYD09GA产品的时间分辨率为天，空间分辨率为500m，波段范围是1-7波段，产品的数据格式为hdf4格式。由于MODIS数据时间分辨率很高，长时间环境变化分析需要处理非常多的文件，例如每天1个文件，20年就需要超过7000个文件，由此，批处理是必须采取的方法。MOD09GA/MYD09GA数据集从NASA官方网站下载后需要经过重投影为UTM，然后再提取各波段数据以便进一步的分析。本软件可以实现批处理将数据投影为UTM，然后提取指定波段，或者多波段同时提取为tif文件。本文档以MOD09GA数据预处理为例，同样适用于MYD09GA数据。
- The MODIS reflectivity product is the most commonly used data in calculating the earth surface albedo, which is divided into MOD09GA and MYD09GA, corresponding to terra and aqua satellites, respectively. The MOD09GA/MYD09GA product has a temporal resolution of one day, 500m spatial resolution, a band range of 1-7 bands, and the product data format in HDF4 format. Due to the high temporal resolution of MODIS data, long-term environmental change analysis needs to process a very large number of files, such as 1 file per day, and more than 7,000 files in 20 years, so batch processing is the method that must be taken. The MOD09GA/MYD09GA dataset downloaded from the official NASA website was reprojected to UTM and then extracted with data from each band for further analysis. This software can implement batch processing to project the data into UTM and then extract the specified bands, or extract multiple bands into TIF files simultaneously.
# 下图是本软件的运行流程示意图
![image](https://user-images.githubusercontent.com/44941550/167147601-ceb910a5-7317-495e-8560-0f43074c998f.png)

# 操作步骤
- （1）运行Anaconda中的Jupyter notebook 
- （2）创建Python3代码
- （3）准备好输入文件
将需要预处理的MOD09GA数据文件放到一个文件夹中，路径仅有英文、数字和下划线这三种类型的字符。
- （4）将代码输入框中并修改代码

①在第24行源代码输入需要提取的子集范围，例如遍历提取11-17子集输入11,18。

②在第41行源代码输入投影类型，例如EPSG:32648 为UTM投影。

③在47-48行代码录入输入和输出路径。
