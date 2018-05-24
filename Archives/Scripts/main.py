import decimales_recuperator
import histogrammes
import randomGenerator
from generator_test import *
"""
Alldata = decimales_recuperator.toData()
histogrammes.prepareToHisto(Alldata)
"""
myGen=randomGenerator.PseudoRandomGenerator()
list=myGen.getRandomList(1000)
print(list)
print(calculate_histo(list))