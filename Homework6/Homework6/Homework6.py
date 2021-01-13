#from scipy.optimize import minimize


#def fun(x,a,b,c):
#    return a*x**2 + b*x + c

#def fun2(a,x,b,c):
#    return a*x**2 + b*x + c

#res=minimize(fun2, 10, args=(1,0,0))
#print(res)
import numpy as np
import pandas as pd
import statsmodels.api as sm

nsample = 100
x = np.linspace(0, 10, 100)
print(x)
#c = np.linspace(1, 1, 100)
#x=[a,c]

beta = np.array([1,0.1])
e = np.random.normal(size=nsample)
X = sm.add_constant(x)
print(X)
y_true=np.dot(X, beta)
#print(y_true)
y = y_true + e


#DF1=pd.read_excel("linear_data.xlsx",sheet_name="data")
##DF1=pd.read_excel("quadric_data01.xlsx",sheet_name="Sheet1")

#x_data=DF1.iloc[:,0]
#c = np.linspace(1, 1, 8)


#x=[x_data,c]
##X = sm.add_constant(x)
#X=np.array(x)

#y_data=DF1.iloc[:,1]

#print(X)
#print(y_data)

model = sm.OLS(y_true, X)
results = model.fit()
print(results.summary())

