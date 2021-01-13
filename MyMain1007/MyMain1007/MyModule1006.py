import MyModules
import numpy as np
import statsmodels.api as sm

def func_1006(x: list, s1:list)->float:
    s2=make_model1004(x)

    t = np.linspace(0,(len(s2)-1)/10,len(s2))
    
    X=np.column_stack((t,s2))
    
    X=sm.add_constant(X)

    
    model = sm.OLS(s1,X)
    results = model.fit()
    
    return results.rsquared

import mislHrf

def make_model1004(x: list)->list:

       
    a1=np.repeat([x[0],x[1],x[2]], 100)
    a2=np.repeat(0,300)

    stim_org=list(np.concatenate([a2,a1,a2], 0))
    HRF=mislHrf.hrf(0.1)

    s1=MyModules.myConv(stim_org,HRF)
    s2=s1[0:901]

    return s2