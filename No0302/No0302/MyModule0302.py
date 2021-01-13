def get_corr(v1,v2):
    import pandas as pd
    V1=pd.Series(v1)
    V2=pd.Series(v2)
    d=V1.corr(V2)
    
    return d