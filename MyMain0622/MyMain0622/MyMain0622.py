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

#DF2～DF5それぞれのCH情報を格納。1つのリストには47個(DFi_CHj)のデータが入る
CH2=[]
CH3=[]
CH4=[]
CH5=[]


for i in range(len(DF7.columns)):
    CH2.append(MyModules.getS(DF7,i))
    CH3.append(MyModules.getS(DF8,i))
    CH4.append(MyModules.getS(DF9,i))
    CH5.append(MyModules.getS(DF10,i))


CH2_filtered=[]
CH3_filtered=[]
CH4_filtered=[]
CH5_filtered=[]

for i in range(len(CH2)):
    CH2_filtered.append(MyModules.butter_bandpass_filter(list(CH2[i]),0.01,0.1,10,5))
    CH3_filtered.append(MyModules.butter_bandpass_filter(list(CH3[i]),0.01,0.1,10,5))
    CH4_filtered.append(MyModules.butter_bandpass_filter(list(CH4[i]),0.01,0.1,10,5))
    CH5_filtered.append(MyModules.butter_bandpass_filter(list(CH5[i]),0.01,0.1,10,5))



S1_ave=MyModules.getDFAverage(DF6)
S2_ave=MyModules.getDFAverage(DF7)
S3_ave=MyModules.getDFAverage(DF8)
S4_ave=MyModules.getDFAverage(DF9)
S5_ave=MyModules.getDFAverage(DF10)

S2_ave_filtered=MyModules.butter_bandpass_filter(list(S2_ave),0.01,0.1,10,5)
S3_ave_filtered=MyModules.butter_bandpass_filter(list(S3_ave),0.01,0.1,10,5)
S4_ave_filtered=MyModules.butter_bandpass_filter(list(S4_ave),0.01,0.1,10,5)
S5_ave_filtered=MyModules.butter_bandpass_filter(list(S5_ave),0.01,0.1,10,5)

DFcorr=pd.DataFrame(data=np.zeros((4,47)))
Si_ave_filtered=[S2_ave_filtered,S3_ave_filtered,S4_ave_filtered,S5_ave_filtered]
CHij_filtered=[CH2_filtered,CH3_filtered,CH4_filtered,CH5_filtered]



for i in range(len(DFcorr)):
    for j in range(len(DFcorr.columns)):
        DFcorr.iat[i,j]=MyModules.get_corr(Si_ave_filtered[i],CHij_filtered[i][j])


print(DFcorr)
