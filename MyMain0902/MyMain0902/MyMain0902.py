import MyModules
import matplotlib.pyplot as plt

base=[0.0,0.5,1.0,0.5,0]
stim=[0.0, 1.0, 0.3, 1.0, 0.5]

plt.plot(base)
plt.show()

plt.plot(MyModules.myConv(stim,base))

plt.show()
