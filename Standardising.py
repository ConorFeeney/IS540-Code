import scipy.stats as st
def standard(data,method):
    """Standarising data using various methods.
    
    Method 1 is MinMax scaling 
    
    Version Control:
    Initial coding
    ------------------------------------------
    Date 4-Feb-18, Author: Conor Feeney, Desc: Initial Coding
    """
    if method == 1:
        X_std = (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))
        data = X_std * (1 - 0) + 0
        return data
    elif method==2:
        data = (data)/(10**len(str(int(max(data)))))
        return data
    elif method ==3:
        data = (data - data.mean(axis=0))/data.std(axis=0)
        data=st.norm.cdf(data)
        return data
    elif method==4:
        return data