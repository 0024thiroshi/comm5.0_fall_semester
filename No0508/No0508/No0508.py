import MyModule0508
import matplotlib.pyplot as plt
Nsample=100
time_step=0.01

a=[10.0,30.0,50.0,120.0]

amp=MyModule0508.get_sin(a,Nsample,time_step)

x=[]
for i in range(Nsample):
   x.append(i*time_step)
plt.plot(x,amp)
plt.show()