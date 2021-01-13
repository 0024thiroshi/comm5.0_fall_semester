def myConv(stim: list, base:list)->list:
    import numpy as np
    conv=np.convolve(stim,base)
    return conv

