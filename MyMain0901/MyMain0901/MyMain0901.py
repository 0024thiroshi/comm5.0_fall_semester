import MyModules
import numpy as np
import matplotlib.pyplot as plt

base=[]

a=[1.0,0.0,0.0,0.0,0.0]

for i in range(1,11):
    base.append(i*0.1)

stim=np.tile(a,5)


plt.plot(MyModules.myConv(stim,base))
plt.show()

