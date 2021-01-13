import numpy as np

n=int(input())

x=np.arange(0.1,0.1*n+0.1,0.1)

X=[]

for i in x:
    X.append(np.array([1,i,i**3]))
print(np.array(X))