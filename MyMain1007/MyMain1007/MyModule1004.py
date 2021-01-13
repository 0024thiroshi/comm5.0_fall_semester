import numpy as np
import MyModules
import mislHrf

def make_model1004(x: list)->list:

       
    a1=np.repeat([x[0],x[1],x[2]], 100)
    a2=np.repeat(0,300)

    stim_org=list(np.concatenate([a2,a1,a2], 0))
    HRF=mislHrf.hrf(0.1)

    s1=MyModules.myConv(stim_org,HRF)
    s2=s1[0:901]

    return s2