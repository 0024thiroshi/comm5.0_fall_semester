import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from sklearn.decomposition import PCA
from pandas import plotting

#データの読み込み
book = pd.ExcelFile("wine.xlsx")
sheet1=book.parse("wine")
myData=sheet1.iloc[:,2:15]

# 主成分分析実行、データを主成分空間に写像
pca = PCA()
pca.fit(myData)
feature = pca.transform(myData)

#第2主成分まででプロット
plt.figure(figsize=(6, 6))
plt.scatter(feature[:, 0], feature[:,1],c=list(sheet1.iloc[:, 0]), alpha=0.5)
plt.grid()
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

#各データ間の相関を見る
plotting.scatter_matrix(pd.DataFrame(feature,columns=["PC{}".format(x + 1) for x in range(len(myData.columns))]),
figsize=(8, 8),c=list(sheet1.iloc[:, 0]), alpha=0.5)
plt.show()

#寄与率の表示
for value in pca.explained_variance_ratio_:
    print(value)