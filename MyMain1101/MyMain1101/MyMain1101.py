import MyModules
DF=MyModules.getDF("dataClustering.xlsx","data")
S1=MyModules.getS(DF,0)
S2=MyModules.getS(DF,1)
MyModules.drawS(S1,S2)
