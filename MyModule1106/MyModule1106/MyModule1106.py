import MyModule11
import matplotlib.pyplot as plt

def draw_data_11(MDS0:MyModule11.My_Data_Set_0):
    CLR=["b","g","r","y","k","c","m","w"]#8色まで対応
    for i in range(MDS0.data_number):
        plt.scatter(MDS0.get_Data(i).coordinate[0],MDS0.get_Data(i).coordinate[1],c=CLR[MDS0.get_Data(i).label])
    plt.show()
    