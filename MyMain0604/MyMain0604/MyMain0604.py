import MyModule0603

from scipy.optimize import minimize
import matplotlib.pyplot as plt
import pandas as pd

x=[1,1,1]


DF1=pd.read_excel("quadric_data01.xlsx",sheet_name="Sheet1")

x_data=DF1.iloc[:,0]
y_data=DF1.iloc[:,1]
plt.scatter(x_data,y_data)



res=minimize(MyModule0603.func03,x,method="SLSQP") 
print(res.x)

yhat_data=res.x[2]*(DF1.iloc[:,0])**2+res.x[1]*DF1.iloc[:,0]+res.x[0]

plt.plot(x_data,yhat_data)

plt.show()


