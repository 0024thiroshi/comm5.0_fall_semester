import MyModule0204
import pandas as pd
DF1=pd.read_excel("nirs.xlsx",sheet_name="Sheet1")
print(MyModule0204.getS(DF1,3))
print(type(MyModule0204.getS(DF1,3)))
