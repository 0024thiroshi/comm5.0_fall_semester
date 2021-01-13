import MyModule0205
import pandas as pd
DF1=pd.read_excel("nirs.xlsx",sheet_name="Sheet1")
print(MyModule0205.extractDF(DF1,1,3))
print(type(MyModule0205.extractDF(DF1,1,3)))

