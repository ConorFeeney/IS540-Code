"""Code to recode the column I3 into industry level.

    Version Control:
    Initial coding
    ------------------------------------------
    Date 8-Feb-18, Author: Danielle Ezzo, Desc: Initial Coding
    """

def Industry_Division(row):
    # Recoding based on table in milestone report
    if row['I3']> 99 and row['I3']< 1000:
         return 'A'
    elif (row['I3']> 999 and row['I3']< 1500):
         return  'B'
    elif (row['I3']> 1499 and row['I3']< 1800):
         return 'C'
    elif (row['I3']> 1999 and row['I3']< 4000):
         return 'D'
    elif (row['I3']> 3999 and row['I3']< 5000):
         return 'E'
    elif (row['I3']> 4999 and row['I3']< 5200):
         return 'F'
    elif (row['I3']> 5199 and row['I3']< 6000):
         return 'G'
    elif (row['I3']> 5999 and row['I3']< 6800):
         return 'H'
    elif (row['I3']> 6999 and row['I3']< 9000):
         return 'I'
    elif (row['I3']> 9099 and row['I3']< 9730):
         return 'J'
    elif (row['I3']> 9899 and row['I3']< 10000):
         return 'K'
    else:
         return 'L'