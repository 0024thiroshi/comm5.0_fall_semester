def func01(x: list, x_data:list, y_data:list)->float:

    sum=0
    for i in range(len(x_data)):
        sum+=(y_data[i]-(x[1]*x_data[i])-x[0])**2

    return sum