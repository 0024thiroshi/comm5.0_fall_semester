import MyModule11
import MyModules

DF=MyModules.getDF("dataClustering.xlsx","data")

MDS0=MyModule11.My_Data_Set_0()
MDS0.cluster_number=4
MDS0.initialization(DF)

MDS0.centroid_procession()

MyModule11.draw_data_11_2(MDS0)
