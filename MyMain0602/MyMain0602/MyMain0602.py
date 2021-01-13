import MyModule0601
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import pandas as pd

x=[1,1]


DF1=pd.read_excel("linear_data.xlsx",sheet_name="data")

x_data=DF1.iloc[:,0]
y_data=DF1.iloc[:,1]
plt.scatter(x_data,y_data)



res=minimize(MyModule0601.func01,x,method="SLSQP") 


linex=[x_data[0],x_data[len(DF1)-1]]
liney=[res.x[1]*x_data[0]+res.x[0],res.x[1]*x_data[len(DF1)-1]+res.x[0]]

plt.plot(linex,liney)

plt.show()


