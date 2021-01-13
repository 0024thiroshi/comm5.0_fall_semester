import MyModules
import numpy as np
import pandas as pd
import mislHrf
import matplotlib.pyplot as plt

stim_org=list(np.repeat([0,1,0],300))

s1=MyModules.myConv(stim_org,list(mislHrf.hrf(0.1)))
s2=s1[:901]

a=float('{:.1f}'.format(len(s2)*0.1))
x=np.arange(0,a,0.1)

plt.plot(x,s2)
plt.show()