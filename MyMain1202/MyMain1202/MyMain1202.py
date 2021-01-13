import MyModules
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np


DF1=MyModules.getDF("dataClustering2.xlsx","data")
DF1=np.array(DF1)


for i in range(5):
    kmeans = KMeans(n_clusters=(i+2), random_state=0)
    clusters = kmeans.fit(DF1)
    
    plt.scatter(i+2,kmeans.inertia_)


plt.show()
