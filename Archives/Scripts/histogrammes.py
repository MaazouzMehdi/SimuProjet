from math import *
import khi2

def prepareToHisto(decimales) :
	fichier2 = open("valeursHisto.dat","w")
	occurrence = khi2.getOccurences(decimales)
	
	for digit in occurrence :
		fichier2.write(str(occurrence[digit]))
		fichier2.write("\n")
	fichier2.close()
