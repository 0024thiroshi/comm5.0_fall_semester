from scipy.optimize import minimize
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm


DF1=pd.read_excel("quadric_data01.xlsx",sheet_name="Sheet1")

x_data=DF1.iloc[:,0]
y_data=DF1.iloc[:,1]

X = np.column_stack((x_data, x_data**2))
X = sm.add_constant(X)
print(X)
print(len(X))


model=sm.OLS(y_data,X)
results=model.fit()
print(results.summary())

plt.scatter(x_data,y_data)
plt.plot(x_data,results.fittedvalues)
plt.show()


#先週との比較
x=[1,1,1]

def func03(x: list)->float:
    import pandas as pd
    DF1=pd.read_excel("quadric_data01.xlsx",sheet_name="Sheet1")

    x_data=DF1.iloc[:,0]
    y_data=DF1.iloc[:,1]

    a=x[2]
    b=x[1]
    c=x[0]

    sum=0
    for i in range(len(DF1)):
        sum+=(y_data[i]-(a*((x_data[i])**2))-b*x_data[i]-c)**2



    return sum


res=minimize(func03,x,method="SLSQP") 
print("")
print("先週との比較")
print(res)

