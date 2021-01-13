import MyModules
import MyModule12
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

n1=1

x_value=MyModule13.fNIRS_opt(ch2,n1)


t = np.linspace(0,(len(ch2[n1])-1)/10,len(ch2[n1]))
value=[]
for i in range(300):
    value.append(0)
for i in range(300):
    value.append(x_value[i])
for i in range(300):
    value.append(0)
plt.bar(t,value)
plt.show()

