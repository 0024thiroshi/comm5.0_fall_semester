import MyModule1006
import MyModules
import pandas as pd

x=[1.0,1.0,1.0]


s1=MyModules.getDF("data1001.xlsx","Sheet1")
s1=list(s1.iloc[:,0])


print(MyModule1006.func_1006(x,s1))
