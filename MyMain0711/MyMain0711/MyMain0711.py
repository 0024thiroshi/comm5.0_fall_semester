import matplotlib.pyplot as plt
from scipy.optimize import minimize
import pandas as pd
import statsmodels.api as sm


x=[1,1]


DF1=pd.read_excel("linear_data.xlsx",sheet_name="data")

x_data=DF1.iloc[:,0]
y_data=DF1.iloc[:,1]
X = sm.add_constant(x_data)


model=sm.OLS(y_data,X)
results = model.fit()

print(results.summary())


plt.scatter(x_data,y_data)
plt.plot(x_data, results.fittedvalues)

plt.show()

#先週の結果との比較

def func01(x:list)->float:
    import pandas as pd
    DF1=pd.read_excel("linear_data.xlsx",sheet_name="data")

    x_data=DF1.iloc[:,0]
    y_data=DF1.iloc[:,1]


    sum=0
    for i in range(len(DF1)):
        sum+=(y_data[i]-(x[1]*x_data[i])-x[0])**2



    return sum

res=minimize(func01,x,method="SLSQP") 

print("")
print("先週の結果との比較")
print(res)

