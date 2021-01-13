def func01(x:list)->float:
    import pandas as pd
    DF1=pd.read_excel("linear_data.xlsx",sheet_name="data")

    x_data=DF1.iloc[:,0]
    y_data=DF1.iloc[:,1]


    sum=0
    for i in range(len(DF1)):
        sum+=(y_data[i]-(x[1]*x_data[i])-x[0])**2



    return sum