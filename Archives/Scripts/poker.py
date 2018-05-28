import decimales_recuperator
from math import pow
import khi2
import util

def proba_r(k,d,r) :
	
	""" Compute the proba to get r (which represents the differents digits in a sequence) """
	
	proba = util.stirling(k,r) * d
	i = 1
	while ( i < r) :
		proba = proba * (d-i)
		i = i+1	
	proba = proba / (pow(d,k)*1.)
	return proba

def create_sequences(decimales) :
	
	""" Create a set of sequences of 5 decimales """
	paquets = []
	compteur = 0
	
	for i in range(0,len(decimales),5) :
		paquets.append(decimales[i:i+5])
	
	return paquets

def calcul_occurrences_theorique(k,d,number_of_sequences) :
	
	""" Compute the theoric occurrences for all r """
	
	res = []
	for i in range(1,6) :
		res.append(proba_r(k,d,i) * number_of_sequences)
	return res
	
def calcul_occurences(paquets) :

	""" Compute the occurrences of r for the all set of sequences """
	
	r = { 1:0, 2:0, 3:0, 4:0, 5:0 }
	
	for i in range(len(paquets)) :
		occurrence = 1
		digits = [paquets[i][0]]
		
		if not(paquets[i][1] in digits):
			occurrence = occurrence +1
			digits.append(paquets[i][1])
		
		if not(paquets[i][2] in digits):
			occurrence = occurrence +1
			digits.append(paquets[i][2])
		
		if not(paquets[i][3] in digits):
			occurrence = occurrence +1
			digits.append(paquets[i][3])
		
		if not(paquets[i][4] in digits):
			occurrence = occurrence +1
			digits.append(paquets[i][4])
		
		r[occurrence] = r[occurrence] + 1
	fichier = open("../Scripts/pokerValues.dat", "w")	
	
	for key in r :
		fichier.write(str(r[key]))
		fichier.write("\n")
	fichier.close()
		
	return r
	

if __name__ == "__main__":
	res = proba(5,10,1)
	res = proba(5,10,2)
	res = proba(5,10,3)
	res = proba(5,10,4)
	res = proba(5,10,5)
	#createPaquet()
	#print(calculOccurences(createPaquet()))
	print(khi2.khi2([13,2644,36172,100670,60501],[20,2700,36000,100800,60480]))
