import mislHrf
import MyModules
import numpy as np
import statsmodels.api as sm

stim1=[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
stim2=[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]
stim3=[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
stim4=[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
stim5=[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]

base=mislHrf.hrf(0.1)

model1=MyModules.myConv(stim1,base)
model2=MyModules.myConv(stim2,base)
model3=MyModules.myConv(stim3,base)
model4=MyModules.myConv(stim4,base)
model5=MyModules.myConv(stim5,base)

models=[model1,model2,model3,model4,model5]

data0904=MyModules.getDF("data0904.xlsx","Sheet1")

x = np.linspace(0,len(data0904)-1,len(data0904))
X=[]

import matplotlib.pyplot as plt

for i in range(5):
   X.append(np.column_stack((x,models[i]))) 
   X[i] = sm.add_constant(X[i])
   model = sm.OLS(data0904, X[i])
   results = model.fit()
   #print(results.summary())
   print(results.rsquared)

   ##ここからは提出していない
   #plt.plot(x,results.fittedvalues,label="model")
   #plt.plot(x,data0904,label="observed")
   plt.scatter(data0904,results.fittedvalues)
   #plt.legend()
   plt.show()






#print(len(model1))
#print(len(data0904))