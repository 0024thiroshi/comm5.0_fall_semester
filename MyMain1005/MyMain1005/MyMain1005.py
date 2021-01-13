import MyModule1004
import MyModules
import numpy as np
import matplotlib.pyplot as plt

x=[1,1,1]
s2=MyModule1004.make_model1004(x)

a=float('{:.1f}'.format(len(s2)*0.1))
t=np.arange(0,a,0.1)

plt.plot(t,s2)
plt.show()
