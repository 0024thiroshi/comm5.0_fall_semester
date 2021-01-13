import MyModules
import matplotlib.pyplot as plt

df=MyModules.getDF("data01.xlsx","Sheet1")

linex=[-1,0,1]
liney=[-2,1,4]

plt.scatter(df.x,df.y)
plt.plot(linex,liney)
plt.show()