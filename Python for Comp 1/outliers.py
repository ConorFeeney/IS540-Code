def outlier(data,method):
    """Deals with outliers in pandas series using differeing methods.
    Only valid for pandas series
    Method 1 is calculating the points that are greater than or less than 3 standard deviations
    away from the mean and setting any values outside this band to be the upper / lower bound 
    (mean+/- 3*standard deviation)
    Method 2 is calculating the points that are greater than or less than 3 standard deviations
    away from the mean and setting any values outside this band to be the mean
    Method 3 is calculating the IQR and finding values outside the limits Q1-IQR*1.5 and Q3+IQR*1.5 
    and setting to be the mean
    Method 4 is calculating the IQR and finding values outside the limits Q1-IQR*1.5 and Q3+IQR*1.5 
    and setting to be the the Q1 or Q3 respectively.
    
    Version Control:
    Initial coding
    ------------------------------------------
    Date 4-Feb-18, Author: Conor Feeney, Desc: Initial Coding
    """
    if data.dtype == float : #Making sure data isnt a string or int
        if method == 1:
            mean, std = data.mean(),data.std() # Creating mean and standard dev variables
            
            #Calculation
            outlier_lower = data< mean-3*std
            outlier_upper = data> mean+3*std
            data[outlier_lower] = mean-3*std
            data[outlier_upper] = mean+3*std
            
        elif method ==2:
            mean, std = data.mean(),data.std()# Creating mean and standard dev variables

            #Calculation
            outlier_lower = data< mean-3*std
            outlier_upper = data> mean+3*std
            data[outlier_lower] = mean
            data[outlier_upper] = mean
            
        elif method == 3:
            # Creating mean and quartile variables
            mean= data.mean()
            lq=data.quantile(0.25)
            uq=data.quantile(0.75)
            iqr = (data.quantile(0.75)- data.quantile(0.25))*1.5
            
            # Calculation
            outlier_lower = data< lq-iqr
            outlier_upper = data> uq+iqr
            data[outlier_lower] = mean
            data[outlier_upper] = mean
            
        elif method ==4:
            # Creating mean and quartile variables
            lq=data.quantile(0.25)
            uq=data.quantile(0.75)
            iqr = (data.quantile(0.75)- data.quantile(0.25))*1.5
            
            #Calculation
            outlier_lower = data< lq-iqr
            outlier_upper = data> uq+iqr
            data[outlier_lower] = lq
            data[outlier_upper] = uq