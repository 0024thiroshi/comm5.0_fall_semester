import numpy as np
import matplotlib.pyplot as plt

def drawMS(ch:list, time_step:float):
    
    
    a=float('{:.1f}'.format(len(ch[1])*time_step))
    x=np.arange(0,a,time_step)
    

    for i in range(len(ch)):
        plt.subplot(1,len(ch),i+1)
        plt.plot(x,ch[i])
    plt.show()
