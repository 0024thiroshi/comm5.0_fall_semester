class My_Data_Point:
    def __init__(self):
        @property #ゲッター
        def label(self):
            return self.__label

        @label.setter #セッター
        def label(self,label):
            self.__label=label

        @property #ゲッター
        def coordinate(self):
            return self.__coordinate

        @coordinate.setter #セッター
        def coordinate(self,coordinate):
            self.__coordinate=coordinate

import random
import pandas as pd

class My_Data_Set_0:
    My_Data_All=[]
    def __init__(self):
        

        @property #ゲッター
        def cluster_number(self):
            return self.__cluster_number

        @cluster_number.setter #セッター
        def cluster_number(self,cluster_number):
            self.__cluster_number=cluster_number

        @property #ゲッター
        def data_number(self):
            return self.__data_number

        @data_number.setter #セッター
        def data_number(self,data_number):
            self.__data_number=data_number



    def initialization(self, DF:pd.DataFrame):
        for i in range(len(DF)):
            MDP=My_Data_Point()
            
            local_label=random.randint(0,self.cluster_number-1)
            local_coordinate=[]
            for j in range(len(DF.columns)):
                local_coordinate.append(DF.iloc[i,j])
            MDP.label=local_label
            MDP.coordinate=local_coordinate  
            self.My_Data_All.append(MDP)
            
        self.data_number=len(DF)

    def get_Data(self, n1:int):
        return self.My_Data_All[n1]

import matplotlib.pyplot as plt

def draw_data_11(MDS0:My_Data_Set_0):
    CLR=["b","g","r","y","k","c","m","w"]#8色まで対応
    for i in range(MDS0.data_number):
        plt.scatter(MDS0.get_Data(i).coordinate[0],MDS0.get_Data(i).coordinate[1],c=CLR[MDS0.get_Data(i).label])
    plt.show()
    