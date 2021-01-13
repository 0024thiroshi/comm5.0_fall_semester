def get_hamming(s1,s2):
    d=0
    for i in range(len(s1)):
        d+=(s1[i]+s2[i])%2
    return d