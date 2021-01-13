from scipy.optimize import minimize
import numpy as np

def getF(v1:list)->float:
    f=5*(v1[0]**2)-6*v1[0]*v1[1]+5*(v1[1]**2)-10*v1[0]+6*v1[1]
    return f


initValue=[10.0,10.0] 

res=minimize(getF, initValue, method="SLSQP") 
print(res)
