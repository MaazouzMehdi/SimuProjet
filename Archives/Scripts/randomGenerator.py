#!/usr/bin/env python
#-*- coding: utf-8 -*-

import math
import time
import random
import logging
from typing import Any


def getPiNumbers(fileN,n):
    """
    read the file and cut in small piece
    :param fileN: adress of the file
    :param n: how much caracter by pieces
    :return: an array with the pieces of pi numbers
    """
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
    """
    class for the pseudo random generator
    """
    def __init__(self,seed=''):
        """
        init of the pseudo random generator
        :param seed: the seed for the generator, if not given aseed will be generated
        """
        self.split = 8
        if seed!='':
            while len(seed)<=6:
                logging.debug("the given seed have a len<=6,  we need to grow her up")
                seed+=seed
            if len(seed)>12:
                logging.debug("the given seed have a len>12,  let’s work with only the last 12 figures")
                seed=seed[-12:]
            try:
                int(seed)
            except ValueError:
                seed=self.generateSeed()
                logging.debug("the given seed isn't a integer, generating a new seed")
            self.seed = seed
        else:
            self.seed = self.generateSeed()
        self.num_list=getPiNumbers("../Enonce/pi6.txt",self.split)

    def generateSeed(self):
        """
        generate a seed with the epoch unix time
        :return: a seed
        """
        seed=str(int(time.time()*math.pow(10,7)%math.pow(10,self.split)))
        while len(str(seed)) <= 6:
            logging.debug("the generated seed have a len<=6,  we need to grow her up")
            seed += seed
        if len(str(seed)) > 12:
            logging.debug("the generated seed have a len>12,  let’s work with only the last 12 figures")
            seed = seed[-12:]
        return seed

    def random(self):
        """

        :return: a generated pseudo random number
        """
        i1=int(self.seed[-6:])%125000
        i2=int(self.seed[:-6])%125000
        res=self.num_list[i1]+self.num_list[i2]
        self.seed=str(int(self.seed)+1)
        return float("0."+res)

    def getRandomList(self,num):
        """
        create an array of generated pseudo random number with my generator
        :param num: how much number is generated
        :return: an array of num generated number
        """
        listrand=[]
        count=0
        while count!=num:
            listrand.append(self.random())
            count+=1
        return listrand

def getPythonRandomList(num):
    """
    create an array of generated pseudo random number with python generator
    :param num: how much number is generated
    :return: an array of num generated number
    """
    listrand=[]
    count=0
    while count!=num:
        listrand.append(random.random())
        count+=1
    return listrand
