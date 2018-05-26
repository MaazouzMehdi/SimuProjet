#!/usr/bin/env python
import math
import logging
from scipy.stats import chi2,kstest,chisquare,ksone
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

def testchi2(value, alpha=0.05):

    n=(len(value))
    chi=0
    tot=0
    for i in range(n):
        tot+=value[i]
    for i in range(n):
        dif=value[i]-tot/n
        den=math.sqrt(tot/n)
        chi+=math.pow(dif/den,2)
    critical = chi2.ppf(1-alpha,n-1)
    result = chi < critical
    logging.debug("test chi2: chi= " + str(chi) + " critical= " + str(critical) + " result= " + str(result))
    return result

def testchi2expected(value, expected, alpha=0.05):

    n=(len(value))
    chi=0
    tot=0
    for i in range(n):
        tot+=value[i]
    for i in range(n):
        diff=value[i]-expected[i]
        chi+=math.pow(diff,2)*1.0/expected[i]
    critical = chi2.ppf(1-alpha,n-1)
    result = chi < critical
    logging.debug("test chi2: chi= " + str(chi) + " critical= " + str(critical) + " result= " + str(result))
    return result

# def kolmotest(value,alpha=0.05):
#     x=kstest(value,"norm")
#     print(x)
#     (ks,pvalue)=x
#     result=pvalue>alpha
#     logging.debug("test kolmogorov-smirnov: ks= " + str(ks) + " pvalue= " + str(pvalue) + " result= " + str(result))
#     logging.debug(len(value))



# def testchi22(value,expectedvalue,alpha=0.05):
#     x=chisquare(value,expectedvalue,ddof=alpha)
#     print(x)
#     # critical = chi2.ppf(1-alpha, (len(value)) - 1)
#     (chi,pvalue)=x
    # print(pvalue)
    # result = chi < critical
    # logging.debug("test chi22: chi= " + str(chi) + " critical= " + str(critical) + " result= " + str(result)+" pvalue= "+str(pvalue))
    # return result

def gapTest(value, a=0.0,b=0.5,t=10,alpha=0.05):
    p=b-a
    length=len(value)
    len_sequence=[0]*t
    n_gap=0
    #calculate the gap
    curr_distance=0
    for i in range(length):
        if not(a<=value[i] and value[i]<b):
            curr_distance+=1
            if i==length-1:
                n_gap+=1
        elif i!=0:
            n_gap+=1
            if curr_distance>=t:
                curr_distance=t-1
            len_sequence[curr_distance]+=1
            curr_distance=0
    #calculate a sequence expected for the chi2 test
    len_expec_sequ=[0]*t
    for i in range(t-1):
        len_expec_sequ[i]=n_gap*p*math.pow(1-p,i)
    len_expec_sequ[t-1]=n_gap*math.pow(1-p,t-1)
    return testchi2expected(len_sequence,len_expec_sequ,alpha)

