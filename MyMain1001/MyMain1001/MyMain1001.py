import mislHrf
import MyModules
import numpy as np
import matplotlib.pyplot as plt

df1=MyModules.getDF("nirs.xlsx","Sheet1")
df1=MyModules.extractDFRow(df1,1,len(df1))
df1=MyModules.extractDF(df1,400,900)

s1=MyModules.getDFAverage(df1)
a=float('{:.1f}'.format(len(s1)*0.1))

x=np.arange(0,a,0.1)

plt.plot(x,s1)
plt.show()

s1.to_excel("data1001.xlsx",index=False)