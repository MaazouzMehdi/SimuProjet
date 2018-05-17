import decimales_recuperator
from sympy.functions.combinatorial.numbers import stirling
from math import pow

def proba(k,d,r) :

	proba = stirling(k,r) * d
	i = 1
	while ( i < r) :
		proba = proba * (d-i)
		i = i+1	
	proba = proba / (pow(d,k)*1.)
	return proba

def createPaquet() :
	res = decimales_recuperator.toData()
	paquets = []
	compteur = 0
	
	for i in range(0,len(res),5) :
		paquets.append(res[i:i+5])
	
	return paquets

def calculOccurences(paquets) :
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
	print(calculOccurences(createPaquet()))
