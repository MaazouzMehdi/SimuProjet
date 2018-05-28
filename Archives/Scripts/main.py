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
decimales = decimales_recuperator.getDecimales()

#Khi2
occurrences_observer = khi2.getOccurences(decimales)
occurrences_theorique = [100000 for i in range(10)]
print(occurrences_theorique)
print(occurrences_observer)

#Test du Poker
sequences = poker.create_sequences(decimales)
occurrences_poker_observer = poker.calcul_occurences(sequences)
occurrences_poker_theorique = poker.calcul_occurrences_theorique(5,10,len(sequences))
print(occurrences_poker_observer)
print(occurrences_poker_theorique)

#Test du collectionneur de coupons
sequences = test_coupon.create_sequences(decimales)
occurrences_coupon_observer = test_coupon.caclul_occurrences(sequences)
occurrences_coupon_theorique = test_coupon.compute_Sr(10,sequences)

#Delete 9 firsts sequences because they are useless
occurrences_coupon_theorique = occurrences_coupon_theorique[9::]
print(occurrences_coupon_observer)
print(occurrences_coupon_theorique)

""" Deuxieme partie : implementation du generateur """

logging.basicConfig( level = logging.DEBUG)
logger = logging.getLogger()


compare_generator("chi",n=10)
compare_generator("gap",n=10)
compare_generator("coupon",n=10)