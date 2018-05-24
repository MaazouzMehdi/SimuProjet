import decimales_recuperator
import histogrammes
import randomGenerator
"""
Alldata = decimales_recuperator.toData()
histogrammes.prepareToHisto(Alldata)
"""
myGen=randomGenerator.PseudoRandomGenerator(seed="123456789")
print(myGen.getRandomList(5))