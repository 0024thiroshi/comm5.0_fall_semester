def myConvError(stim:list, base:list, data:list)->float:
    import numpy as np
    
    conv=np.convolve(stim,base)
    sum=0
    
    for i in range(len(data)):
        sum+=(data[i]-conv[i])**2
    return sum

