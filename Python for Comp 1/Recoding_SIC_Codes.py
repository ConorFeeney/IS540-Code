"""Code to recode the column I3 into industry level.

    Version Control:
    Initial coding
    ------------------------------------------
    Date 8-Feb-18, Author: Danielle Ezzo, Desc: Initial Coding
    """

def Industry_Division(row):

    if row['I3']> 99 and row['I3']< 1000:
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