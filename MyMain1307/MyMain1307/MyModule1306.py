
import MyModule12
from scipy.optimize import minimize

def fNIRS_opt(ch_data:list, n1:int)->list:
    
    coef=[]
    for i in range(300):
        coef.append(1)
    
    bounds=[]
    for i in range(300):
        bounds.append(np.array([0,1]))


    res=minimize(MyModule12.func_12,coef,args=ch_data[n1],bounds=bounds)

    return res.x
