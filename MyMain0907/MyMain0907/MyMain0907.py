import mislHrf
import MyModules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s1=MyModules.getDF("data0906.xlsx","Sheet1")
s1=MyModules.getS(s1,0)
print(len(s1))

s2=pd.Series(MyModules.butter_bandpass_filter(s1,0.01,0.1,10),name="Ch2")


x=np.arange(0,len(s2)*0.1,0.1)
#print(type(x))



plt.plot(x,s2)
plt.show()

s2.to_excel("data0907.xlsx",index=False)