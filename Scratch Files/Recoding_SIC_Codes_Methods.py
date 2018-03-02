"""Code to recode the column I3 into industry level.

    Version Control:
    Initial coding
    ------------------------------------------
    Date 8-Feb-18, Author: Danielle Ezzo, Desc: Initial Coding
    """

def Industry_Division(row,method):
    # Recoding based on table in milestone report
    if method==1:
        if (row['I3']> 99 and row['I3']< 1000):
            return 'Agriculture, Forestry and Fishing'
        elif (row['I3']> 999 and row['I3']< 1500):
            return  'Mining'
        elif (row['I3']> 1499 and row['I3']< 1800):
            return 'Construction'
        elif (row['I3']> 1999 and row['I3']< 4000):
            return 'Manufacturing'
        elif (row['I3']> 3999 and row['I3']< 5000):
            return 'Transportation, Communications, Electric, Gas and Sanitary service'
        elif (row['I3']> 4999 and row['I3']< 5200):
            return 'Wholesale Trade'
        elif (row['I3']> 5199 and row['I3']< 6000):
            return 'Retail Trade'
        elif (row['I3']> 5999 and row['I3']< 6800):
            return 'Finance, Insurance and Real Estate'
        elif (row['I3']> 6999 and row['I3']< 9000):
            return 'Services'
        elif (row['I3']> 9099 and row['I3']< 9730):
            return 'Public Administration'
        elif (row['I3']> 9899 and row['I3']< 10000):
            return 'Nonclassifiable'
        else:
            return 'Missing'
    elif method==2:
        if (row['I3']> 1999 and row['I3']< 4000):
            return 'Manufacturing'
        else:
            return 'Other'
    elif method==3:
        if (row['I3']> 7369 and row['I3']< 7375) :
            return 'Tech'
        else:
            return 'NonTech'
    elif method==4:
        if (row['I3']> 1999 and row['I3']< 4000):
            return 'Manufacturing' # Manufacturing
        elif (row['I3']> 3999 and row['I3']< 5000):
            return 'Services' # Tech Comms etc Services
        elif (row['I3']> 6999 and row['I3']< 9000):
            return 'Services' #Services (combining with above)
        else:
            return 'Other' # All Other
    elif method==5:
        if(row['I3']> 1999 and row['I3']< 4000):
            return 'Manufacturing'
        elif (row['I3']> 3999 and row['I3']< 5000):
            return 'Services' #TCEGS
        elif (row['I3']> 4999 and row['I3']< 5200):
            return 'Trade' #wholesale
        elif (row['I3']> 5199 and row['I3']< 6000):
            return 'Trade' #retail
        elif (row['I3']> 6999 and row['I3']< 9000):
            return 'Services'
        else:
            return 'Other'
    elif method==6:
        if(row['I3']> 1999 and row['I3']< 4000):
            return 'Manufacturing'
        elif (row['I3']> 3999 and row['I3']< 5000):
            return 'TCEGS' 
        elif (row['I3']> 4999 and row['I3']< 5200):
            return 'Trade' #wholesale
        elif (row['I3']> 5199 and row['I3']< 6000):
            return 'Trade' #retail
        elif (row['I3']> 6999 and row['I3']< 9000):
            return 'Services'
        else:
            return 'Other'
    elif method==7:
        if (row['I3']> 99 and row['I3']< 5000):
            return 'Manual Labor'
        else: 
            return 'NonManual Labor'
        