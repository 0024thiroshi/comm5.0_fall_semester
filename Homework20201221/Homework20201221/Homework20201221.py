import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.datasets import load_iris
import pandas as pd

df=pd.read_excel("dataClustering.xlsx",name="data")



# 階層型クラスタリングの実施
# ウォード法 x ユークリッド距離
linkage_result = linkage(df, method='ward', metric='euclidean')
print(linkage_result)

# クラスタ分けするしきい値を決める
threshold = 0.6*np.max(linkage_result[:, 2])

# 階層型クラスタリングの可視化
plt.figure(num=None, figsize=(16, 9), dpi=200, facecolor='w', edgecolor='k')
dendrogram(linkage_result, color_threshold=threshold)
plt.show()

# クラスタリング結果の値を取得
clustered = fcluster(linkage_result, threshold, criterion='distance')

# クラスタリング結果を比較
print(clustered)



#from sklearn.cluster import KMeans
 
#import pandas as pd
#df=pd.read_excel("dataClustering.xlsx",name="data")


#kmeans = KMeans(n_clusters=4, random_state=0)
#clusters = kmeans.fit(df)
#df['cluster'] = clusters.labels_
 
#print(df['cluster'].unique())
#print(df)










#import numpy as np
#import pandas as pd

#import random
#x0=[]
#x1=[]
#x2=[]
#for i in range(50):
#    x0.append(random.randint(1,100))
#    x1.append(x0[i]+random.randint(1,10))
#    x2.append(x0[i]-random.randint(1,10))

#x0=np.array(x0)
#x1=np.array(x1)
#x2=np.array(x2)
##print(type(x0))
##x=np.array(x0,x1)
#X=np.array([x0,x1,x2])
##print(X)

##Xは2行50列のデータセットとする
#d = 3
#n = 50
##print(pd.Series.corr(pd.Series(X[0]),pd.Series(X[1])))
##print(pd.Series.corr(pd.Series(X[2]),pd.Series(X[1])))
##print(pd.Series.corr(pd.Series(X[0]),pd.Series(X[2])))
## 平均ベクトル
#mu = np.mean(X, axis=1).reshape((d, 1))    # (2, 1)これは行数と列数を表す

## 共分散行列
#Sigma = np.dot((X - mu), (X - mu).T) / n  # (2, 2)
##print(Sigma)

## 無相関化
#lam, S = np.linalg.eig(Sigma)  # 固有値分解にて、固有値・固有ベクトルに分解

##print(lam)

##print(S)



#X_dash = np.dot(S.T, X)  # (2, 50)
##print(pd.Series.corr(pd.Series(X_dash[0]),pd.Series(X_dash[1])))
##print(pd.Series.corr(pd.Series(X_dash[2]),pd.Series(X_dash[1])))
##print(pd.Series.corr(pd.Series(X_dash[0]),pd.Series(X_dash[2])))

## 白色化
#Lambda = np.diag(lam)  # 固有値の対角化


#X_dash = np.dot(np.linalg.inv(np.sqrt(Lambda)),np.dot(S.T, (X - mu)))

#print(X_dash)

##print(pd.Series.corr(pd.Series(X_dash[0]),pd.Series(X_dash[1])))
##print(pd.Series.corr(pd.Series(X_dash[2]),pd.Series(X_dash[1])))
##print(pd.Series.corr(pd.Series(X_dash[0]),pd.Series(X_dash[2])))