import random
import pandas as pd
import MyModule11

class My_Data_Set_0:
    My_Data_All=[]
    centroid_points=[]

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
            MDPG=MyModule11.My_Data_Point()
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


                MDPG.coordinate.append(sum/len(My_Data_All_k))
                

            self.centroid_points.append(MDPG)
           

    def get_centroid_points(self):
        return self.centroid_points