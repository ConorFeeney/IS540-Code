def SICClusters(data,method):
"""Code to recode the column I3 into industry level.

    Version Control:
    Initial coding
    ------------------------------------------
    Date 8-Feb-18, Author: Danielle Ezzo, Desc: Initial Coding
    """
if method == 1:

    ipo_data['SICCluster'] = ipo_data.apply(Tech, axis=1)

elif method == 2:

    ipo_data['SICCluster'] = ipo_data.apply(Manufacturing, axis=1)
    
elif method == 3:

    ipo_data['SICCluster'] = ipo_data.apply(IndCluster3, axis=1)
    
  