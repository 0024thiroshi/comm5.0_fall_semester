from scipy.signal import butter,lfilter 

def fNIRS_bandbass(ch_data:list, low_f: float, high_f:float, time_step:float, order:int)->list:
    ch2=[]
    for i in range(len(ch_data)):
        ch2.append(butter_bandpass_filter(ch_data[i],low_f,high_f,1/time_step, order))
    return ch2

def butter_bandpass(lowcut,highcut, fs, order):
    nyq = 0.5*fs 
    low = lowcut/nyq 
    high = highcut/nyq 
    b,a = butter(order,[low, high],btype='band') 
    return b,a

def butter_bandpass_filter(data,lowcut,highcut, fs, order): 
    b, a = butter_bandpass(lowcut,highcut, fs, order=order) 
    y = lfilter(b, a, data) 
    return y

