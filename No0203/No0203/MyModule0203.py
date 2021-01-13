def getDF(file_name,sheet_name):
    import pandas as pd
    DF1=pd.read_excel(file_name,sheet_name=sheet_name)
    return DF1
