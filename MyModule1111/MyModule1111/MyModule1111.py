#最終的にMyModule11はこの形になりました

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
    centroid_points=[]
    iFlag=0

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

    def centroid_procession(self):
        self.centroid_points=[]
        for k in range(self.cluster_number):
            MDPG=My_Data_Point()
            My_Data_All_k=[]
            MDPG.coordinate=[]
            MDPG.label=k
            for i in range(len(self.My_Data_All)):
                if self.My_Data_All[i].label==k:
                    My_Data_All_k.append(self.My_Data_All[i])
         
        
            for i in range(len(self.My_Data_All[1].coordinate)):
                
                
                
                sum=0
                for j in range(len(My_Data_All_k)):
                    sum+=My_Data_All_k[j].coordinate[i]

                if len(My_Data_All_k)==0:
                    print("label{0}のデータの個数が0になりました。座標(0,0)を重心として計算します".format(k))
                    MDPG.coordinate.append(sum/(len(My_Data_All_k)+1))
                else:
                    MDPG.coordinate.append(sum/len(My_Data_All_k))
                

            self.centroid_points.append(MDPG)
           

    def get_centroid_points(self):
        return self.centroid_points

    
    def assign_label(self):
        import math
        self.iFlag=0
        

        for i in range(len(self.My_Data_All)):
            distance=[]
            min_dis=99999
            n1=9
            for j in range(self.cluster_number):
                distance.append(math.sqrt(((self.centroid_points[j].coordinate[0])-self.My_Data_All[i].coordinate[0])**2+((self.centroid_points[j].coordinate[1])-self.My_Data_All[i].coordinate[1])**2))
                if min_dis>distance[j]:
                    min_dis=distance[j]
                    n1=j
            if self.My_Data_All[i].label!=n1:
                self.iFlag=1
                self.My_Data_All[i].label=n1

    def get_label_flag(self):
        return self.iFlag

import matplotlib.pyplot as plt

def draw_data_11(MDS0:My_Data_Set_0):
    CLR=["b","g","r","y","k","c","m","w"]#8色まで対応
    for i in range(MDS0.data_number):
        plt.scatter(MDS0.get_Data(i).coordinate[0],MDS0.get_Data(i).coordinate[1],c=CLR[MDS0.get_Data(i).label])
    plt.show()
    
def draw_data_11_2(MDS0:My_Data_Set_0):
    CLR=["b","g","r","y","k","c","m","w"]#8色まで対応
    for i in range(MDS0.data_number):
        plt.scatter(MDS0.get_Data(i).coordinate[0],MDS0.get_Data(i).coordinate[1],c=CLR[MDS0.get_Data(i).label])

    for i in range(MDS0.cluster_number):
        plt.scatter(MDS0.get_centroid_points()[i].coordinate[0],MDS0.get_centroid_points()[i].coordinate[1],c=CLR[MDS0.get_centroid_points()[i].label],marker="*")
          
    plt.show()
    


