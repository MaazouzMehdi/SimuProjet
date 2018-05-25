#!/usr/bin/env python
import math
from scipy.stats import chi2
import matplotlib.pyplot as plt

def calculate_histo(list):
    occur=[0]*10
    for i in range(len(list)):
        if list[i]<0.1:
            occur[0]+=1
        elif list[i]<0.2:
            occur[1]+=1
        elif list[i]<0.3:
            occur[2]+=1
        elif list[i]<0.4:
            occur[3]+=1
        elif list[i]<0.5:
            occur[4]+=1
        elif list[i]<0.6:
            occur[5]+=1
        elif list[i]<0.7:
            occur[6]+=1
        elif list[i]<0.8:
            occur[7]+=1
        elif list[i]<0.9:
            occur[8]+=1
        else:
            occur[9]+=1
    return occur

def testchi2(value,expected, alpha=0.05):

    n=(min(len(value),len(expected)))
    chi=0
    for i in range(n):
        dif=value[i]-expected[i]
        chi+=math.pow(dif,2)*1.0/expected[i]
    critical = chi2.ppf(1-alpha,n-1)
    result= chi <critical


    return result

