import MyModule0605

from scipy.optimize import minimize
import matplotlib.pyplot as plt
import pandas as pd

x=[1,1,1]


DF1=pd.read_excel("quadric_data01.xlsx",sheet_name="Sheet1")


x_data=DF1.iloc[:,0]
y_data=DF1.iloc[:,1]
plt.scatter(x_data,y_data)


res=minimize(MyModule0605.func05,x,method="SLSQP") 


yhat_data=res.x[2]*(5*(DF1.iloc[:,0])-1)**2+res.x[1]*DF1.iloc[:,0]+res.x[0]



plt.plot(x_data,yhat_data)

plt.show()



