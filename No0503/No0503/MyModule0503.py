def getD0503():
    from numpy.linalg import solve
    import math
    
    b=(3*0.783+0.2)/3

    left=[[3,-1],[1/3,1]]
    right=[-1,b]

    print(solve(left, right))

    d=abs(3*0.2-0.783+1)/math.sqrt(3**2+(-1)**2)
    
    print(d**2)