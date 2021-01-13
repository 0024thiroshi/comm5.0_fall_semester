import MyModule1006
import MyModules
from scipy.optimize import minimize

s1=MyModules.getDF("data1001.xlsx","Sheet1")
s1=list(s1.iloc[:,0])

res=minimize(MyModule1006.func_1006,[10,10,10], args=s1)

print(res.x)
print(MyModule1006.func_1006(res.x,s1))
