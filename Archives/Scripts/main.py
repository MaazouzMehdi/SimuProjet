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
list=myGen.getRandomList(1000)
histo=calculate_histo(list)
print(list)
print(histo)
#print(testchi2(histo,[100]*10,0.05))
res1=[0,0]
res2=[0,0]
for i in range(50):
    print(i)
    myGen = randomGenerator.PseudoRandomGenerator()
    list = myGen.getRandomList(10000)
    histo = calculate_histo(list)
    # print(histo)
    chi=testchi2(histo)
    if chi:
        res1[0]+=1
    else:
        res1[1]+=1
    # listpy=randomGenerator.getPythonRandomList(100000)
    # histopy = calculate_histo(listpy)
    # # print(histopy)
    # chi = testchi2(histopy)
    # if chi:
    #     res2[0] += 1
    # else:
    #     res2[1] += 1

print(res1)
# print(res2)