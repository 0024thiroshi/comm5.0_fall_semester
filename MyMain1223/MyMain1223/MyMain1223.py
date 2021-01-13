import MyModules
import mislHrf
import MyModule1222
import numpy as np
import matplotlib.pyplot as plt

s1=MyModules.getDF("data1212.xlsx","Sheet1")

x=list(np.repeat(1,300))
s2=MyModule1222.make_model12(x)

a=float('{:.1f}'.format(len(s2)*0.1))
t=np.arange(0,a,0.1)

plt.subplot(1,2,1)
plt.plot(t,s1)
plt.legend("observed")

plt.subplot(1,2,2)
plt.plot(t,s2)
plt.legend("model")
plt.show()

