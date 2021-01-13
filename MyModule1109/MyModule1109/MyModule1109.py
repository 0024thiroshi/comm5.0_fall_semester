import MyModule11

def draw_data_11_2(MDS0:MyModule11.My_Data_Set_0):
    CLR=["b","g","r","y","k","c","m","w"]#8色まで対応
    for i in range(MDS0.data_number):
        plt.scatter(MDS0.get_Data(i).coordinate[0],MDS0.get_Data(i).coordinate[1],c=CLR[MDS0.get_Data(i).label])

    for i in range(MDS0.cluster_number):
        plt.scatter(MDS0.get_centroid_points()[i].coordinate[0],MDS0.get_centroid_points()[i].coordinate[1],c=CLR[MDS0.get_centroid_points()[i].label],marker="*")
          
    plt.show()
    