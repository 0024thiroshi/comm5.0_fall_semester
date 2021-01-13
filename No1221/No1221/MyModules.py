

def getDF(file_name,sheet_name):
    import pandas as pd
    DF1=pd.read_excel(file_name,sheet_name=sheet_name)
    return DF1



def getS(DF,n1):
    import pandas as pd
    S1=pd.Series(DF.iloc[:,n1])
    return S1

def extractDF(DF,n1,n2):
    DF2=DF.iloc[n1:n1+n2,:]
    return DF2



def drawS(S1,S2):
    import matplotlib.pyplot as plt

    if len(S1)==len(S2):
        plt.scatter(S1,S2)
        plt.show()
    else:
        print("2つのSeriesのサイズが異なります")


def extractDFRow(DF,n1,n2):
    
    DF2=DF.iloc[:,n1:n1+n2]
    return DF2


        

def getDFAverage(DF):
    import pandas as pd
    a=[]
    for i in range(len(DF)):
        a.append(sum(DF.iloc[i])/len(DF.iloc[i]))
    S1=pd.Series(a)
    return S1

def get_corr(v1,v2):
    import pandas as pd
    V1=pd.Series(v1)
    V2=pd.Series(v2)
    d=V1.corr(V2)
    
    return d

import pandas as pd

def compoundSeries(s1: pd.Series, s2:pd.Series)->pd.DataFrame:
   
    df=pd.DataFrame([s1,s2])
    return df

def get_sin(a: list, Nsample: int, time_step: float)->list:
    import math

    amp=[0]*Nsample   
    
    for i in range(len(a)):
        for j in range(Nsample):
            amp[j]+=(math.sin(2*math.pi*a[i]*j*time_step))

    return amp

from scipy.signal import butter,lfilter 

def butter_bandpass(lowcut,highcut, fs, order=3):
    nyq = 0.5*fs 
    low = lowcut/nyq 
    high = highcut/nyq 
    b,a = butter(order,[low, high],btype='band') 
    return b,a

def butter_bandpass_filter(data,lowcut,highcut, fs, order=3): 
    b, a = butter_bandpass(lowcut,highcut, fs, order=3) 
    y = lfilter(b, a, data) 
    return y

def myConv(stim: list, base:list)->list:
    import numpy as np
    conv=np.convolve(stim,base)
    return conv



def myConvError(stim:list, base:list, data:list)->float:
    import numpy as np
    
    conv=np.convolve(stim,base)
    sum=0
    
    for i in range(len(data)):
        sum+=(data[i]-conv[i])**2
    return sum







