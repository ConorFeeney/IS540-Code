"""Code to recode the column I3 into Manufacturer vs Non Manufacturer level.

    Version Control:
    Initial coding
    ------------------------------------------
    Date 8-Feb-18, Author: Danielle Ezzo, Desc: Initial Coding
    """

def Manufacturing(row):
    
    if (row['I3']> 1999 and row['I3']< 4000):
        return 1
    else:
        return 0