import MyModules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import fftpack

s1=MyModules.getDF("data1001.xlsx","Sheet1")
s2=MyModules.butter_bandpass_filter(s1.iloc[:,0],0.01,0.1,10)
#
#MyModulesではorderが5で固定だったので、MyModulesの方でorderを3に変えました

a=float('{:.1f}'.format(len(s2)*0.1))
x=np.arange(0,a,0.1)

plt.subplot(1,2,1)
plt.plot(x,s1,label="s1")
plt.plot(x,s2,label="s2")
plt.xlabel("time[s]")
plt.ylabel("Power")
plt.legend()


S1 = fftpack.fft(s1)
S2 = fftpack.fft(s2)
S1=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S1])
S2=np.array([np.sqrt(c.real ** 2 + c.imag ** 2) for c in S2])
freq = fftpack.fftfreq(len(s1),0.1)

plt.subplot(1,2,2)
plt.plot(freq,S1,label="s1")
plt.plot(freq,S2,label="s2")


plt.legend()
plt.xlabel("frequency[Hz]")
plt.ylabel("Power")
plt.show()

s2=pd.Series(s2)
s2.to_excel("data1212.xlsx",index=False)

