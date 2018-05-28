import decimales_recuperator
import khi2
import histogrammes
import poker
import test_coupon
import randomGenerator
from generator_test import *
import logging
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy

""" Premiere partie : calcul du caractere pseudo aleatoire de pi """
# decimales = decimales_recuperator.getDecimales()
#
# #Khi2
# occurrences_observer = khi2.getOccurences(decimales)
# occurrences_theorique = [100000 for i in range(10)]
# #print(occurrences_theorique)
# #print(occurrences_observer)
#
# #Test du Poker
# sequences = poker.create_sequences(decimales)
# occurrences_poker_observer = poker.calcul_occurences(sequences)
# occurrences_poker_theorique = poker.calcul_occurrences_theorique(5,10,len(sequences))
# #print(occurrences_poker_observer)
# #print(occurrences_poker_theorique)
#
# #Test du collectionneur de coupons
# sequences = test_coupon.create_sequences(decimales)
# occurrences_coupon_observer = test_coupon.caclul_occurrences(sequences)
# occurrences_coupon_theorique = test_coupon.compute_Sr(10,sequences)
#
# #Delete 9 firsts sequences because they are useless
# occurrences_coupon_theorique = occurrences_coupon_theorique[9::]
# #print(occurrences_coupon_observer)
# #print(occurrences_coupon_theorique)

""" Deuxieme partie : implementation du generateur """

logging.basicConfig( level = logging.DEBUG)
logger = logging.getLogger()


#
# myGen=randomGenerator.PseudoRandomGenerator()
# # # print(myGen.random())
# list=myGen.getRandomList(100000)
# list=randomGenerator.getPythonRandomList(100000)
# histo=calculate_histo(list)
# plt.hist(list,10,color = 'red',edgecolor = 'black')

#
# plt.ylabel("Nombre d'occurence")
# plt.title("Nombre d'occurence des nombres généré par notre générateur ")
# plt.xlabel("Ecart (par 0.1)")
# plt.axis([0,1,9500,10500])
# pp = PdfPages('multipage.pdf')
# pp.savefig()
# pp.close()
# plt.show()
# print(histo)
# pourcen=[0]*10
# for i in range(10):
#     pourcen[i]=(histo[i]-10000)/1000
# print(pourcen)
#
# testchi2(histo)
#
# gapTest(list)
#
# coupon_test(list)
res=[0,0]
for i in range(100):
    # myGen = randomGenerator.PseudoRandomGenerator()
    list = randomGenerator.getPythonRandomList(100000)
    # histo = calculate_histo(list)
    if coupon_test(list):
        res[0]+=1
    else:
        res[1]+=1
print(res)