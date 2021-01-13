import pandas as pd

def getDFAverage(DF):
    a=[]
    for i in range(len(DF)):
        a.append(sum(DF.iloc[i])/len(DF.iloc[i]))
    S1=pd.Series(a)
    return S1

