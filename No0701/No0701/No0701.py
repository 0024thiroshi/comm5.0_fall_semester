import MyModule0701
from scipy.optimize import minimize
import pandas as pd

DF1=pd.read_excel("linear_data.xlsx",sheet_name="data")
x_data=DF1.iloc[:,0]
y_data=DF1.iloc[:,1]

x=[0,0]

res=minimize(MyModule0701.func01,x,args=(x_data,y_data),method="SLSQP")
print(res)
