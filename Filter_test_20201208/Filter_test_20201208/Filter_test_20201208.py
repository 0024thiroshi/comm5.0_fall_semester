import MyModules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a=[0.1,0.3,0.5]

sin=np.array(MyModules.get_sin(a,900,0.01))
plt.plot(sin)



sinf=np.array(MyModules.butter_bandpass_filter(sin,0.2,0.4,100))
plt.plot(sinf)
plt.show()

