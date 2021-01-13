#import numpy as np
#a = np.array([0, 1, 2, 3, 4, 5]) # 配列a
#v = np.array([0.2, 0.1,0.3]) # 配列v
#res=np.convolve(a,v, mode='valid') 
#print(res)

import numpy as np
a = np.array([0, 1, 2])
#print(np.tile(a, 2)) # 1次元配列を２回繰り返す。



print(np.tile(a,(3,2)))
