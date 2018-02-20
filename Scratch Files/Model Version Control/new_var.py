import numpy as np
from scipy import stats
import pandas as pd
"""
Code to create our target and control variables using the data dictionary as reference

 Version Control:
    Initial coding
    ------------------------------------------
    Date 2-Feb-18, Author: Conor Feeney, Desc: Initial Coding
    Date 5-Feb-18, Author: Daneille Ezzo, Desc: Edition Target and Control group code for efficiency
    """

def y1function(row):
    """Function to create Target Variable Y1
    """
    row['P(mid)']=(row['P(H)']+row['P(L)'])/2
    if row['P(IPO)'] < row['P(mid)']:
        #If statement to determine value setting 
        val = 1
    else:
        val = 0
    return val


def y2function(row):
    """Function to create Target Variable Y2
    """
    if row['P(IPO)'] < row['P(1Day)']:
        #If statement to determine value setting 
        val = 1
    else:
        val = 0
    return val




def C3function(row):
    """Function to create C3
    """
    if row['C3'] >=0:
        #If statement to determine value setting 
        val = 1
    else:
        val = 0
    return val

def C6function(row):
    """Function to create C6
    """
    row['P(mid)']=(row['P(H)']+row['P(L)'])/2#Creating midpoint
    if row['P(IPO)'] > row['P(mid)']:
        #If statement to determine value setting 
        val = ((row['P(IPO)']-row['P(mid)'])/row['P(mid)'])
    else:
        val = 0
    return val

def calc(x):
    """function to calculate ratios and share overhang"""
    x['C5x']=x['C5']/x['C6']#Share Overhang
    x['T3x']=x['T3']/x['T2']#Ratio of Real words
    x['T4x']=x['T4']/x['T1']#Ratio of long sentences
    x['T5x']=x['T5']/x['T2']#Ratio of long words
    x['S1x']=x['S1']/x['T2']#Ratio of postive words
    x['S2x']=x['S2']/x['T2']#Ratio of negative wors
    x['S3x']=x['S3']/x['T2']#Ratio of uncertain words