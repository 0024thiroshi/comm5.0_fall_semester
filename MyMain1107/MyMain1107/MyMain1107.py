import MyModules
import MyModule11

DF=MyModules.getDF("dataClustering.xlsx","data")

MDS0=MyModule11.My_Data_Set_0()
MDS0.cluster_number=4
MDS0.initialization(DF)

MyModule11.draw_data_11(MDS0)