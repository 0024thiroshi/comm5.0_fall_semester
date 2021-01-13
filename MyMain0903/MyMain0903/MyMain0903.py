import MyModules
import mislHrf
import matplotlib.pyplot as plt

stim=[1.0]

for i in range(49):
    stim.append(0.0)

stim.append(1.0)

base=mislHrf.hrf(0.1)

plt.plot(MyModules.myConv(stim,base))
plt.show()