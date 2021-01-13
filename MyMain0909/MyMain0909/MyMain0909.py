import MyModules
import mislHrf
import numpy as np
import statsmodels.api as sm

model_data=MyModules.getDF("data0908.xlsx","Sheet1")
observed_data=MyModules.getDF("data0907.xlsx","Sheet1")



x = np.linspace(0,len(model_data)-1,len(model_data))
X=np.column_stack((x,model_data))
X = sm.add_constant(X)

model = sm.OLS(observed_data,X)
results = model.fit()

print("beta2=",results.params[2])
print("r2=",results.rsquared)

   
   
