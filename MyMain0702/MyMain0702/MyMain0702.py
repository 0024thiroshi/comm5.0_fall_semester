import MyModule0701
from scipy.optimize import minimize
import pandas as pd
import matplotlib.pyplot as plt

DF1=pd.read_excel("linear_data.xlsx",sheet_name="data")
x_data=DF1.iloc[:,0]
y_data=DF1.iloc[:,1]
plt.scatter(x_data,y_data)

x=[0,0]

res=minimize(MyModule0701.func01,x,args=(x_data,y_data),method="SLSQP")
print(res)

linex=[x_data[0],x_data[len(DF1)-1]]
liney=[res.x[1]*x_data[0]+res.x[0],res.x[1]*x_data[len(DF1)-1]+res.x[0]]

plt.plot(linex,liney)

plt.show()

