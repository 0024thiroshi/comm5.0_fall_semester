import numpy as np
import matplotlib.pyplot as plt

def drawMS(ch:list, time_step:float):
    
    
    a=float('{:.1f}'.format(len(ch[1])*time_step))
    x=np.arange(0,a,time_step)
    

    for i in range(len(ch)):
        plt.subplot(1,len(ch),i+1)
        plt.plot(x,ch[i])
    plt.show()

from scipy.signal import butter,lfilter 

def fNIRS_bandbass(ch_data:list, low_f: float, high_f:float, time_step:float, order:int)->list:
    ch2=[]
    for i in range(len(ch_data)):
        ch2.append(butter_bandpass_filter(ch_data[i],low_f,high_f,1/time_step, order))
    return ch2

def butter_bandpass(lowcut,highcut, fs, order):
    nyq = 0.5*fs 
    low = lowcut/nyq 
    high = highcut/nyq 
    b,a = butter(order,[low, high],btype='band') 
    return b,a

def butter_bandpass_filter(data,lowcut,highcut, fs, order): 
    b, a = butter_bandpass(lowcut,highcut, fs, order=order) 
    y = lfilter(b, a, data) 
    return y


import MyModule12
from scipy.optimize import minimize

def fNIRS_opt(ch_data:list, n1:int)->list:
    
    coef=[]
    for i in range(300):
        coef.append(1)
    
    bounds=[]
    for i in range(300):
        bounds.append(np.array([0,1]))


    res=minimize(MyModule12.func_12,coef,args=ch_data[n1],bounds=bounds)

    return res.x



