def get_sin(a: list, Nsample: int, time_step: float)->list:
    import math

    amp=[0]*Nsample   
    
    for i in range(len(a)):
        for j in range(Nsample):
            amp[j]+=(math.sin(2*math.pi*a[i]*j*time_step))

    return amp


import matplotlib.pyplot as plt
from scipy import fftpack
import numpy as np

Nsample=100
time_step=0.001

a=[10.0,30.0,50.0,120.0]

A=get_sin(a,Nsample,time_step)
x=[]
for i in range(Nsample):
    x.append(i*time_step)

plt.plot(x,A)

plt.show()

AMP = fftpack.fft(A) 
freqlist=fftpack.fftfreq(Nsample, d=time_step)

AS=[np.sqrt(c.real ** 2 + c.imag ** 2) for c in AMP] 
AS2=np.array(AS)



plt.plot(freqlist,AS2)
plt.show()



def  getDataN1N2(data,lowcut,highcut,fs,order):
    from scipy.signal import butter,lfilter 
    def butter_bandpass(lowcut,highcut, fs, order=order): 
        nyq = 0.5*fs 
        low = lowcut/nyq 
        high = highcut/nyq 
        b,a = butter(order,[low, high],btype='band') 
        return b,a

    def butter_bandpass_filter(data,lowcut,highcut, fs, order=order): 
        b, a = butter_bandpass(lowcut,highcut, fs, order=order) 
        y = lfilter(b, a, data) 
        return y

    data2 = butter_bandpass_filter(data,lowcut,highcut,fs,order=order)
    return data2

A2=getDataN1N2(A,15.0,100.0,1/time_step,8)
AMP2= fftpack.fft(A2) 
AS3=[np.sqrt(c.real ** 2 + c.imag ** 2) for c in AMP2] 
AS4=np.array(AS3)


plt.plot(freqlist,AS4)
plt.show()