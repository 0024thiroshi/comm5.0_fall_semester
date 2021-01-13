import MyModules
import numpy as np
import mislHrf

def make_model12(x: list)->list:

    a2=np.repeat(0,300)
    a3=a2
    for i in range(len(x)):
        a1=np.array(x[i])
        a3=np.hstack((a3,a1))
    stim_org=list(np.hstack((a3,a2)))
    
    HRF=mislHrf.hrf(0.1)

    s1=MyModules.myConv(stim_org,HRF)
    s2=s1[0:901]

    return s2

def func_12(x: list, s1:list)->float:
    s2=make_model12(x)

    t = np.linspace(0,(len(s2)-1)/10,len(s2))
    
    X=np.column_stack((t,s2))
    
    X=sm.add_constant(X)

    
    model = sm.OLS(s1,X)
    results = model.fit()
    
    return 1/results.rsquared
