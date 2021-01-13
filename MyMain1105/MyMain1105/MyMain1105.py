import MyModule11
import MyModules

DF=MyModules.getDF("dataClustering.xlsx","data")

MDS0=MyModule11.My_Data_Set_0()
MDS0.cluster_number=4
MDS0.initialization(DF)


print(MDS0.cluster_number)
print(MDS0.data_number)

print("")
for i in range(MDS0.data_number):
    print(MDS0.get_Data(i).label)
    print(MDS0.get_Data(i).coordinate)