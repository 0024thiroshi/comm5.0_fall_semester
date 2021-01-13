import pandas as pd
import math

def getD(xx:pd.Series, yy:pd.Series, a:float, b:float)->float:

    d=[]
    sum=0

    for i in range(len(xx)):
        d.append(abs(a*xx[i]-yy[i]+b)/math.sqrt(a**2+(-1)**2))
        sum+=d[i]
        
    return sum
