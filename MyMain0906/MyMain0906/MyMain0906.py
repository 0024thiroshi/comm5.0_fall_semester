import MyModules
import mislHrf
import matplotlib.pyplot as plt
import numpy as np

df1=MyModules.getDF("nirs.xlsx","Sheet1")
df1=MyModules.extractDF(df1,400,901)

s1=MyModules.getS(df1,2)


x=np.arange(0,len(s1)*0.1,0.1)


plt.plot(x,s1)
plt.show()

s1.to_excel("data0906.xlsx",index=False)
