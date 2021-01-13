from scipy.optimize import minimize
import numpy as np
import pandas as pd
import MyModule0504
import matplotlib.pyplot as plt

xx=pd.Series([-1.000 , -0.900, -0.800, -0.700, -0.600, -0.500, - 0.400, -0.300, -0.200, -0.100, -0.000, 0.100 , 0.200,0.300 , 0.400 , 0.500 , 0.600 , 0.700, 0.800, 0.900])
yy=pd.Series([-1.656 , -0.734 , -3.036 , -1.026 , -1.104 , 0.023 ,0.246 , 1.817 , 0.651 , 0.082 , 2.524 , 2.231 ,0.783,2.489 , 1.892 , 3.207 , 1.868 , 3.954 , 4.447 , 4.024])


for a in range(100):
    plt.scatter(a/10,MyModule0504.getD(xx,yy,a/10,1),c="blue")
plt.show()
