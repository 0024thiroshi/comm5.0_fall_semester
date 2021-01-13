import MyModules

DF=MyModules.getDF("nirs.xlsx","Sheet1")
DF1=MyModules.extractDF(DF,1,100)
DF2=MyModules.extractDF(DF,101,300)
DF3=MyModules.extractDF(DF,401,300)
DF4=MyModules.extractDF(DF,701,300)
DF5=MyModules.extractDF(DF,1001,300)

DF_100=MyModules.extractDF(DF,1,100)
DF_300=MyModules.extractDF(DF,1,300)

T1_100=MyModules.getS(DF_100,0)
T1_300=MyModules.getS(DF_300,0)

T1_100=T1_100*0.1
T1_300=T1_300*0.1


DF6=MyModules.extractDFRow(DF1,1,47)
DF7=MyModules.extractDFRow(DF2,1,47)
DF8=MyModules.extractDFRow(DF3,1,47)
DF9=MyModules.extractDFRow(DF4,1,47)
DF10=MyModules.extractDFRow(DF5,1,47)

S6=MyModules.getDFAverage(DF6)
S7=MyModules.getDFAverage(DF7)
S8=MyModules.getDFAverage(DF8)
S9=MyModules.getDFAverage(DF9)
S10=MyModules.getDFAverage(DF10)

#フィルター前の時系列描画

MyModules.drawS(T1_100,S6)
MyModules.drawS(T1_300,S7)
MyModules.drawS(T1_300,S8)
MyModules.drawS(T1_300,S9)
MyModules.drawS(T1_300,S10)

from scipy import fftpack
import numpy as np
import pandas as pd

freqlist_100=fftpack.fftfreq(100,d=0.1)
freqlist_300=fftpack.fftfreq(300,d=0.1)

S6_F=fftpack.fft(list(S6))
S7_F=fftpack.fft(list(S7))
S8_F=fftpack.fft(list(S8))
S9_F=fftpack.fft(list(S9))
S10_F=fftpack.fft(list(S10))

AS6=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S6_F])
AS7=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S7_F])
AS8=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S8_F])
AS9=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S9_F])
AS10=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S10_F])

#フィルター前の周波数描画
MyModules.drawS(freqlist_100,AS6)
MyModules.drawS(freqlist_300,AS7)
MyModules.drawS(freqlist_300,AS8)
MyModules.drawS(freqlist_300,AS9)
MyModules.drawS(freqlist_300,AS10)


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

S6_f=getDataN1N2(list(S6),0.01,0.1,10,5)
S7_f=getDataN1N2(list(S7),0.01,0.1,10,5)
S8_f=getDataN1N2(list(S8),0.01,0.1,10,5)
S9_f=getDataN1N2(list(S9),0.01,0.1,10,5)
S10_f=getDataN1N2(list(S10),0.01,0.1,10,5)


#フィルター後の時系列描画
MyModules.drawS(T1_100,S6_f)
MyModules.drawS(T1_300,S7_f)
MyModules.drawS(T1_300,S8_f)
MyModules.drawS(T1_300,S9_f)
MyModules.drawS(T1_300,S10_f)


S6_fF=fftpack.fft(list(S6_f))
S7_fF=fftpack.fft(list(S7_f))
S8_fF=fftpack.fft(list(S8_f))
S9_fF=fftpack.fft(list(S9_f))
S10_fF=fftpack.fft(list(S10_f))

AS6_f=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S6_fF])
AS7_f=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S7_fF])
AS8_f=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S8_fF])
AS9_f=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S9_fF])
AS10_f=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S10_fF])


#フィルター後の周波数描画
MyModules.drawS(freqlist_100,AS6_f)
MyModules.drawS(freqlist_300,AS7_f)
MyModules.drawS(freqlist_300,AS8_f)
MyModules.drawS(freqlist_300,AS9_f)
MyModules.drawS(freqlist_300,AS10_f)