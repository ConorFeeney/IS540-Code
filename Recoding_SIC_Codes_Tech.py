"""Code to recode the column I3 into Tech vs Non-Tech Companies.

    Version Control:
    Initial coding
    ------------------------------------------
    Date 21-Feb-18, Author: Danielle Ezzo, Desc: Initial Coding
    """

def Tech(row):
    ## checking on definition of tech companies 
    if (row['I3']> 7369 and row['I3']< 7375) :
        return 1
    else:
        return 0