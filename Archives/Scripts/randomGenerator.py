#!/usr/bin/env python

import math
import time
import random
import logging
from typing import Any


def getPiNumbers(fileN,n):

    file=open(fileN,'r')
    num_list=[]  # type: str
    eof = False
    count=0
    val=""
    while not eof:
        r=file.read(1)
        if not r:
            eof = True
        else:
            asc= ord(r)
            if(47<asc) and (asc<58):
                count+=1
                val+=r
                if count==n:
                    num_list.append(val)
                    count=0
                    val=""
    file.close()
    return num_list

class PseudoRandomGenerator(object):
    def __init__(self,seed='',n=8):
        self.split = n
        if seed!='':
            try:
                seed=int(seed)
            except ValueError:
                seed=self.generateSeed()
                logging.debug("the given seed isn't a integer, generating a new seed")
            self.seed = seed
        else:
            self.seed = self.generateSeed()


        self.num_list=getPiNumbers("../Enonce/pi6.txt",n)
        self.seed=self.seed%len(self.num_list)

    def generateSeed(self):
        return int(time.time()*math.pow(10,7)%math.pow(10,self.split))

    def random(self):
        num=self.num_list[self.seed]
        # val=math.pow(num,4)
        # val=math.pow(num,3)*self.seed
        strval=str(int(num))
        res=float("0."+strval[1:])

        self.seed+=1
        if self.seed>=len(self.num_list):
            self.seed
        return res

    def getRandomList(self,num):
        listrand=[]
        count=0
        while count!=num:
            listrand.append(self.random())
            count+=1
        return listrand

def getPythonRandomList(num):
    listrand=[]
    count=0
    while count!=num:
        listrand.append(random.random())
        count+=1
    return listrand