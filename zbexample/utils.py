from scipy import signal

def detrend(x,*args,**kwargs):
    return(signal.detrend(x,*args,**kwargs))
