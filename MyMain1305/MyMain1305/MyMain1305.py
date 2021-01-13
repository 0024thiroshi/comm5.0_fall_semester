import MyModules
import MyModule13

import numpy as np
import matplotlib.pyplot as plt

df1=MyModules.getDF("nirs.xlsx","Sheet1")
df1=MyModules.extractDFRow(df1,1,len(df1))
df1=MyModules.extractDF(df1,400,900)

ch=[]
for i in range(len(df1.columns)):
    ch.append(df1.iloc[:,i])



ch2=MyModule13.fNIRS_bandbass(ch,0.01,0.1,0.1,3)
MyModule13.drawMS(ch2,0.1)