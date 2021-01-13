import numpy as np
import pandas as pd
import sklearn 
from sklearn.decomposition import PCA #主成分分析
import matplotlib.pyplot as plt 
df=pd.read_excel("seiseki.xlsx",sheet_name="seiseki")

# 主成分分析実行
pca = PCA()
feature = pca.fit(df)
# データを主成分空間に写像
feature = pca.transform(df)
#print(feature)

#第2主成分まででプロット
plt.figure(figsize=(6, 6))
plt.scatter(feature[:, 0], feature[:, 1], alpha=0.8, c=list(df.iloc[:, 0]))
plt.grid()
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

#主成分表示
print(pca.components_)
print("")
#平均表示
print(pca.mean_)
print("")
#共分散行列表示
print(pca.get_covariance())
print("")

#寄与率表示
print(pca.explained_variance_ratio_)

