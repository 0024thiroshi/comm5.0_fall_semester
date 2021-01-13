import MyModules

DF=MyModules.getDF("nirs.xlsx","Sheet1")
DF1=MyModules.extractDF(DF,1,100)
DF2=MyModules.extractDF(DF,101,300)
DF3=MyModules.extractDF(DF,401,300)
DF4=MyModules.extractDF(DF,701,300)
DF5=MyModules.extractDF(DF,1001,300)

DF_100=MyModules.extractDF(DF,1,100)
DF_300=MyModules.extractDF(DF,1,300)

T1_100=MyModules.getS(DF_100,0)
T1_300=MyModules.getS(DF_300,0)

T1_100=T1_100*0.1
T1_300=T1_300*0.1


DF6=MyModules.extractDFRow(DF1,1,47)
DF7=MyModules.extractDFRow(DF2,1,47)
DF8=MyModules.extractDFRow(DF3,1,47)
DF9=MyModules.extractDFRow(DF4,1,47)
DF10=MyModules.extractDFRow(DF5,1,47)

S6=MyModules.getDFAverage(DF6)
S7=MyModules.getDFAverage(DF7)
S8=MyModules.getDFAverage(DF8)
S9=MyModules.getDFAverage(DF9)
S10=MyModules.getDFAverage(DF10)

MyModules.drawS(T1_100,S6)
MyModules.drawS(T1_300,S7)
MyModules.drawS(T1_300,S8)
MyModules.drawS(T1_300,S9)
MyModules.drawS(T1_300,S10)
