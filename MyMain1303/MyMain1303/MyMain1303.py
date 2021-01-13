import MyModules
import MyModule12
import MyModule13
import mislHrf

import numpy as np
import matplotlib.pyplot as plt

df1=MyModules.getDF("nirs.xlsx","Sheet1")
df1=MyModules.extractDFRow(df1,1,len(df1))
df1=MyModules.extractDF(df1,400,900)

ch=[]
for i in range(len(df1.columns)):
    ch.append(df1.iloc[:,i])

MyModule13.drawMS(ch,0.1)