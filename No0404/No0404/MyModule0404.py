import pandas as pd

def compoundSeries(s1: pd.Series, s2:pd.Series)->pd.DataFrame:
 
    df=pd.DataFrame([s1,s2])
    return df