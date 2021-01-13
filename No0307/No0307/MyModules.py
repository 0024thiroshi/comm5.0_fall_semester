

def getDF(file_name,sheet_name):
    import pandas as pd
    DF1=pd.read_excel(file_name,sheet_name=sheet_name)
    return DF1



def getS(DF,n1):
    import pandas as pd
    S1=pd.Series(DF.iloc[:,n1])
    return S1

def extractDF(DF,n1,n2):
    DF2=DF.iloc[n1:n1+n2,:]
    return DF2



def drawS(S1,S2):
    import matplotlib.pyplot as plt

    if len(S1)==len(S2):
        plt.scatter(S1,S2)
        plt.show()
    else:
        print("2つのSeriesのサイズが異なります")


def extractDFRow(DF,n1,n2):
    
    DF2=DF.iloc[:,n1:n1+n2]
    return DF2


        

def getDFAverage(DF):
    import pandas as pd
    a=[]
    for i in range(len(DF)):
        a.append(sum(DF.iloc[i])/len(DF.iloc[i]))
    S1=pd.Series(a)
    return S1

