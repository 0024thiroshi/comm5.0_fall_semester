import scipy
import numpy as np
from math import exp
import pandas as pd
import scipy.stats as sps
import matplotlib.pyplot as plt
import math

def hrf(nt,
        peak_delay=6,
        under_delay=10,
        p_u_ratio = 6,):#nt:時間間隔
    t = np.arange(0,30+nt,nt)
    peak_disp=1
    under_disp=1
    normalize=True    
                  
    hrf = np.zeros(t.shape, dtype=np.float)
    
    pos_t = t[t > 0]
    peak = sps.gamma.pdf(pos_t,
                         peak_delay/peak_disp,
                         loc=0,
                         scale=peak_disp)
    UD = under_delay + peak_delay
    undershoot = sps.gamma.pdf(pos_t,
                               UD / under_disp,
                               loc=0,
                               scale=under_disp)
    hrf = peak - undershoot / p_u_ratio
    if not normalize:
        return hrf
    return hrf / np.max(hrf)









