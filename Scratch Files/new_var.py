import numpy as np
from scipy import stats
import pandas as pd

def calc(x):
    x['Y1']=''
    for i in range(len(x['P(IPO)'])):
        if x['P(IPO)'][i]<((x['P(H)'][i]+x['P(L)'][i])/2):
            x['Y1'][i]=1
        else:
            x['Y1'][i]=0
    x.Y1 = x.Y1.astype(int)
    print(x['Y1'])

    x['Y2']=''
    for i in range(len(x['P(IPO)'])):
        if x['P(IPO)'][i]<x['P(1Day)'][i]:
            x['Y2'][i]=1
        else:
            x['Y2'][i]=0
    x.Y2 = x.Y2.astype(int)
    print(x['Y2'])

    x['C3x']=''
    for i in range(len(x['P(IPO)'])):
        if x['C3'][i]>0:
            x['C3x'][i]=1
        else:
            x['C3x'][i]=0
    x.C3x = x.C3x.astype(int)
    print(x['C3x'])

    x['C6x']=''
    mid=(x['P(H)']+x['P(L)'])/2
    for i in range(len(x['P(IPO)'])):    
        if x['P(IPO)'][i]>mid[i]:
            x['C6x'][i]=((x['P(IPO)'][i]-mid[i])/(mid[i]*100))
        else:
            x['C6x'][i]=0
    #x.C6x = x.C6x.astype(float)
    print(x['C6x'])

    x['C5x']=x['C5']/x['C6']
    x['T3x']=x['T3']/x['T2']
    x['T4x']=x['T4']/x['T1']
    x['T5x']=x['T5']/x['T2']
    x['S1x']=x['S1']/x['T2']
    x['S2x']=x['S2']/x['T2']
    x['S3x']=x['S3']/x['T2']