import MyModules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s1=MyModules.getDF("data1001.xlsx","Sheet1")
s2=pd.Series(MyModules.butter_bandpass_filter(s1.iloc[:,0],0.01,0.1,10))

a=float('{:.1f}'.format(len(s2)*0.1))
x=np.arange(0,a,0.1)

plt.plot(x,s1,label="s1")
plt.plot(x,s2,label="s2")
plt.legend()
plt.show()


s2.to_excel("data1002.xlsx",index=False)