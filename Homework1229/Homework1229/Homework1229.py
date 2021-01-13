
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("dataClustering2.xlsx",name="data")

# 階層型クラスタリングの実施、ウォード法 x ユークリッド距離
linkage_result = linkage(df, method='ward', metric='euclidean')
print(linkage_result)

# クラスタ分けする閾値を決める
threshold = 0.1*np.max(linkage_result[:, 2])

# 階層型クラスタリングの可視化
plt.figure(num=None, figsize=(16, 9), dpi=200, facecolor='w', edgecolor='k')
dendrogram(linkage_result, color_threshold=threshold)
plt.show()

clustered = fcluster(linkage_result, threshold, criterion="distance") # クラスタリング結果の値を取得
print(clustered) # クラスタリング結果を比較

