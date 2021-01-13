import MyModule11
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
            MDP=MyModule11.My_Data_Point()
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
