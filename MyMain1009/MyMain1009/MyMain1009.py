import MyModules
import MyModule1006
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import numpy as np



s1=MyModules.getDF("data1001.xlsx","Sheet1")
s1=list(s1.iloc[:,0])

a=float('{:.1f}'.format(len(s1)*0.1))
t=np.arange(0,a,0.1)

res=minimize(MyModule1006.func_1006,[1,1,1], args=s1)


plt.plot(t,s1,label="observed")
plt.plot(t,MyModule1006.make_model1004([1,1,1]),label="1,1,1")
plt.plot(t,MyModule1006.make_model1004(res.x),label="minimized")
plt.legend()

plt.show()







