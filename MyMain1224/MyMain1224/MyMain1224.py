import MyModules
import mislHrf
import MyModule1222

import matplotlib.pyplot as plt
from scipy.optimize import minimize
import numpy as np

coef=[]
for i in range(300):
    coef.append(1)

coef_1=[]
for i in range(300):
    coef_1.append(1)

s1=MyModules.getDF("data1212.xlsx","Sheet1")
s1=list(s1.iloc[:,0])

a=float('{:.1f}'.format(len(s1)*0.1))
t=np.arange(0,a,0.1)

bounds=[]
for i in range(300):
    bounds.append(np.array([0,1]))

res=minimize(MyModule1222.func_12,coef,args=s1,bounds=bounds)

print(res.x)
print(MyModule1222.func_12(res.x,s1))





