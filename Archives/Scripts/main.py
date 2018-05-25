import decimales_recuperator
import histogrammes
import randomGenerator
from generator_test import *
"""
Alldata = decimales_recuperator.toData()
histogrammes.prepareToHisto(Alldata)
"""
#myGen=randomGenerator.PseudoRandomGenerator()
#list=myGen.getRandomList(1000)
# histo=calculate_histo(list)
#print(testchi2(histo,[100]*10,0.05))
res=[0,0]
for i in range(1000):
    myGen = randomGenerator.PseudoRandomGenerator()
    list = myGen.getRandomList(1000)
    histo = calculate_histo(list)
    chi=testchi2(histo, [100] * 10, 0.05)
    if chi:
        res[0]+=1
    else:
        res[1]+=1
    print(i)
print(res)