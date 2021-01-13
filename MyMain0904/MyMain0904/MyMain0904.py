import mislHrf
import MyModules
import pandas as pd

stim=[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]
base=mislHrf.hrf(0.1)

data0904=MyModules.myConv(stim,base)


df = pd.DataFrame(data0904,columns=["data0904"])

df.to_excel("data0904.xlsx",index=False)

