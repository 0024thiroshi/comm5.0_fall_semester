from abc import ABCMeta,abstractmethod
import math


class Distance_Func:
    @abstractmethod
    def get_distance(self, v1, v2):
        pass

class Euclidean_Distance(Distance_Func):  
    def get_distance(self,v1,v2):
        d=0        
        for i in range(len(v1)):
            d+=(v1[i]-v2[i])**2
        d=math.sqrt(d)
        return d