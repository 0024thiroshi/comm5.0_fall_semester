import MyModules
from scipy import fftpack
import numpy as np
import pandas as pd


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


S1_ave=MyModules.getDFAverage(DF6)
S2_ave=MyModules.getDFAverage(DF7)
S3_ave=MyModules.getDFAverage(DF8)
S4_ave=MyModules.getDFAverage(DF9)
S5_ave=MyModules.getDFAverage(DF10)

#フィルター前の時系列データ
MyModules.drawS(T1_300,S2_ave)
MyModules.drawS(T1_300,S3_ave)
MyModules.drawS(T1_300,S4_ave)
MyModules.drawS(T1_300,S5_ave)

freqlist_100=fftpack.fftfreq(100,d=0.1)
freqlist_300=fftpack.fftfreq(300,d=0.1)

S2_ave_F=fftpack.fft(list(S2_ave))
S3_ave_F=fftpack.fft(list(S3_ave))
S4_ave_F=fftpack.fft(list(S4_ave))
S5_ave_F=fftpack.fft(list(S5_ave))

AS2_ave_F=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S2_ave_F])
AS3_ave_F=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S3_ave_F])
AS4_ave_F=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S4_ave_F])
AS5_ave_F=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S5_ave_F])


#フィルター前の周波数描画
MyModules.drawS(freqlist_300,AS2_ave_F)
MyModules.drawS(freqlist_300,AS3_ave_F)
MyModules.drawS(freqlist_300,AS4_ave_F)
MyModules.drawS(freqlist_300,AS5_ave_F)


S2_ave_filtered=MyModules.butter_bandpass_filter(list(S2_ave),0.01,0.1,10,5)
S3_ave_filtered=MyModules.butter_bandpass_filter(list(S3_ave),0.01,0.1,10,5)
S4_ave_filtered=MyModules.butter_bandpass_filter(list(S4_ave),0.01,0.1,10,5)
S5_ave_filtered=MyModules.butter_bandpass_filter(list(S5_ave),0.01,0.1,10,5)



#フィルター後の時系列描画
MyModules.drawS(T1_300,S2_ave_filtered)
MyModules.drawS(T1_300,S3_ave_filtered)
MyModules.drawS(T1_300,S4_ave_filtered)
MyModules.drawS(T1_300,S5_ave_filtered)


S2_ave_filtered_F=fftpack.fft(list(S2_ave_filtered))
S3_ave_filtered_F=fftpack.fft(list(S3_ave_filtered))
S4_ave_filtered_F=fftpack.fft(list(S4_ave_filtered))
S5_ave_filtered_F=fftpack.fft(list(S5_ave_filtered))

AS2_ave_filtered_F=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S2_ave_filtered_F])
AS3_ave_filtered_F=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S3_ave_filtered_F])
AS4_ave_filtered_F=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S4_ave_filtered_F])
AS5_ave_filtered_F=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S5_ave_filtered_F])


#フィルター後の周波数描画

MyModules.drawS(freqlist_300,AS2_ave_filtered_F)
MyModules.drawS(freqlist_300,AS3_ave_filtered_F)
MyModules.drawS(freqlist_300,AS4_ave_filtered_F)
MyModules.drawS(freqlist_300,AS5_ave_filtered_F)
