import MyModules
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np


DF1=MyModules.getDF("dataClustering2.xlsx","data")
DF1=np.array(DF1)


kmeans = KMeans(n_clusters=3, random_state=0)#クラスター数を指定
clusters = kmeans.fit(DF1)	 #クラスタリングを実行



c=["r","b","y","g","k","m"]

for i in range(len(DF1)):
    plt.scatter(DF1[i,0],DF1[i,1],c=c[clusters.labels_[i]])


for i in range(3):
    plt.scatter(kmeans.cluster_centers_[i,0],kmeans.cluster_centers_[i,1],c=c[i],marker="*")
plt.show()