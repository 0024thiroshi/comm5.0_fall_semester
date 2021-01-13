def getS(DF,n1):
    import pandas as pd
    S1=pd.Series(DF.iloc[:,n1])
    return S1
