#!/usr/bin/env python
import math
import logging
from scipy.stats import chi2,kstest,chisquare,ksone
import matplotlib.pyplot as plt
from util import *



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



def coupon_test(value,d=10,t=45,alpha=0.05):
    length = len(value)
    curr_values=[0]*(t-(d-1)-1)
    complete_sequ=0
    occurence=[False]*d
    count=0
    count_sequ=0

    for i in range(length):
        count += 1
        num=int(math.floor(d*value[i]))
        if occurence[num]==False:
            count_sequ += 1
            occurence[num]=True
            if count_sequ==d:
                complete_sequ+=1
                if count>=t-1:
                    curr_values[t-d-1]+=1
                else:
                    curr_values[count-d]+=1
                occurence=[False]*d
                count=0
                count_sequ=0
    expected = [0] * (t - (d - 1) - 1)
    for i in range(len(expected) - 1):
        expected[i] = complete_sequ*((math.factorial(d)/math.pow(d,(i + d)))*stirling((i+d)-1,d-1))
    expected[len(expected)-1]=complete_sequ*(1.0-(math.factorial(d)/math.pow(d,(len(expected)-1+d)-2))*stirling((len(expected)-1+d)-2,d))
    return testchi2expected(curr_values,expected,alpha)