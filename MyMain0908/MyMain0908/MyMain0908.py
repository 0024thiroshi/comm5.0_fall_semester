import MyModules
import mislHrf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

stim=np.repeat([0.0,1.0,0.0],300)
base=mislHrf.hrf(0.1)


s3=list(np.convolve(stim,base,mode ='same'))
s3.append(0.0)
s3=pd.Series(s3,name="Ch2")
print(len(s3))


x=np.arange(0,len(s3)*0.1,0.1)


plt.plot(x,s3)
plt.show()

s3.to_excel("data0908.xlsx",index=False)