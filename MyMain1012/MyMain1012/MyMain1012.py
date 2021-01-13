import MyModules
import MyModule1011
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import numpy as np

coef=[]
for i in range(300):
    coef.append(i)

coef_1=[]
for i in range(300):
    coef_1.append(1)

s1=MyModules.getDF("data1001.xlsx","Sheet1")
s1=list(s1.iloc[:,0])

a=float('{:.1f}'.format(len(s1)*0.1))
t=np.arange(0,a,0.1)

res=minimize(MyModule1011.func_1011,coef,args=s1)

print(res.x)
print(MyModule1011.func_1011(res.x,s1))


