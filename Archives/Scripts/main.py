import decimales_recuperator
import khi2
import histogrammes
import poker
import test_coupon
import randomGenerator
from generator_test import *
import logging
"""
Alldata = decimales_recuperator.toData()
histogrammes.prepareToHisto(Alldata)
"""

""" Premiere partie : calcul du caractere pseudo aleatoire de pi """
decimales = decimales_recuperator.getDecimales()

#Khi2
occurrences_observer = khi2.getOccurences(decimales)
occurrences_theorique = [100000 for i in range(10)]
#print(occurrences_theorique)
#print(occurrences_observer)

#Test du Poker
sequences = poker.create_sequences(decimales)
occurrences_poker_observer = poker.calcul_occurences(sequences)
occurrences_poker_theorique = poker.calcul_occurrences_theorique(5,10,len(sequences))
#print(occurrences_poker_observer)
#print(occurrences_poker_theorique)

#Test du collectionneur de coupons
sequences = test_coupon.create_sequences(decimales)
occurrences_coupon_observer = test_coupon.caclul_occurrences(sequences)
occurrences_coupon_theorique = test_coupon.compute_Sr(10,sequences)

#Delete 9 firsts sequences because they are useless
occurrences_coupon_theorique = occurrences_coupon_theorique[9::]
#print(occurrences_coupon_observer)
#print(occurrences_coupon_theorique)

""" Deuxieme partie : implementation du generateur """

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
