def getDNA(n1):
    List=[]
    import random
    for i in range(n1):
        j=random.randint(0,3)
        if j==0:
            List.append("A")
        elif j==1:
            List.append("T")
        elif j==2:
            List.append("C")
        elif j==3:
            List.append("G")
        else:
            pass
    return List
