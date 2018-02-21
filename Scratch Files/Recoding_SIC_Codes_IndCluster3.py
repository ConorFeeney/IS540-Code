"""Code to recode the column I3 into Industry Clusters with 3 levels

    Version Control:
    Initial coding
    ------------------------------------------
    Date 21-Feb-18, Author: Danielle Ezzo, Desc: Initial Coding
    """

def IndCluster3(row):
    
    if (row['I3']> 1999 and row['I3']< 4000):
        return 1 # Manufacturing
    elif (row['I3']> 3999 and row['I3']< 5000):
        return 2 # Tech Comms etc Services
    elif (row['I3']> 6999 and row['I3']< 9000):
        return 2 #Services (combining with above)
    else:
        return 3 # All Other