from scipy.optimize import minimize

import numpy as np


def getF(v1:list)->float:
    f=(v1[0]-1)**2+(v1[1]-3)**2
    return f

def conF(v1:list)->float:
    f=v1[0]+v1[1]-1
    return f

cons = (
    {'type': 'ineq', 'fun': conF}
)#v1[0]+v1[1]-1≥0を表す。ineqは≥0を、eqは=0を表す




initValue=[1.0, 1.0]
mybounds = [[1,2],[1,2]]

res=minimize(getF, initValue, method='BFGS')

#res=minimize(getF, initValue, method='SLSQP',constraints=cons)
print(res)



#def getF(v1:list)->float:
#    f=(v1[0]-1)**2+(v1[1]-3)**2
#    return f


#initValue=[1.0, 1.0] #x1=1.0,x2=1.0を初期値とする
#mybounds = [[1,2],[1,2]] #それぞれ、x1の最小値、最大値　及びx2の最小値、最大値
#res=minimize(getF, initValue, method="L-BFGS-B",bounds=mybounds) #getFの値を最小とするx1,x2を求める
#print(res)
