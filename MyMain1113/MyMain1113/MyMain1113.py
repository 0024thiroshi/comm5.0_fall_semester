import MyModule11
import MyModules

DF=MyModules.getDF("dataClustering.xlsx","data")

MDS0=MyModule11.My_Data_Set_0()
MDS0.cluster_number=4
MDS0.initialization(DF)
n1=1

while n1==1:
    MDS0.centroid_procession()
    MyModule11.draw_data_11_2(MDS0)
    MDS0.assign_label()
    n1=MDS0.get_label_flag()
    


