def func05(x: list)->float:
    import pandas as pd
    DF1=pd.read_excel("quadric_data01.xlsx",sheet_name="Sheet1")

    x_data=DF1.iloc[:,0]
    y_data=DF1.iloc[:,1]

    a=x[2]
    b=x[1]
    c=x[0]

    sum=0
    for i in range(len(DF1)):
        sum+=(y_data[i]-a*((5*(x_data[i])-1)**2)-b*x_data[i]-c)**2



    return sum



