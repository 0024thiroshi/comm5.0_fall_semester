def get_sin(a: list, Nsample: int, time_step: float)->list:
    import math

    amp=[0]*Nsample   
    
    for i in range(len(a)):
        for j in range(Nsample):
            amp[j]+=(math.sin(2*math.pi*a[i]*j*time_step))

    return amp
