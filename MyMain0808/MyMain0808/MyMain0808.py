import numpy as np

stim1=np.repeat(3, 10)
print(stim1)

stim2=np.repeat(0,51)
print(stim2)

stim2[0]=1.0
stim2[25]=1.0
stim2[50]=1.0
print(stim2)
