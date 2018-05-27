import decimales_recuperator
import histogrammes
import randomGenerator
from generator_test import *
import logging
"""
Alldata = decimales_recuperator.toData()
histogrammes.prepareToHisto(Alldata)
"""
logging.basicConfig( level = logging.DEBUG)
logger = logging.getLogger()



myGen=randomGenerator.PseudoRandomGenerator()
# print(myGen.random())
list=myGen.getRandomList(10000)
coupon_test(list)
# test=[4,11,9,5,8,13, 17,13,15,5]
# kolmotest(test)
# histo=calculate_histo(list)
# print(list)
# print(histo)
# test=[4,11,9,5,8,13,17,13,15,5]
# testchi2(histo)
# testchi22(histo)
# testchi22(test,0.02)
# res1=[0,0]
# res2=[0,0]
# for i in range(50):
#     print(i)
#     myGen = randomGenerator.PseudoRandomGenerator()
#     list = myGen.getRandomList(100)
#     histo = calculate_histo(list)
#     # print(histo)
#     chi=testchi2(histo)
#     if chi:
#         res1[0]+=1
#     else:
#         res1[1]+=1
#     listpy=randomGenerator.getPythonRandomList(100)
#     histopy = calculate_histo(listpy)
#     # print(histopy)
#     chi = testchi2(histopy)
#     if chi:
#         res2[0] += 1
#     else:
#         res2[1] += 1
#
# print(res1)
# print(res2)