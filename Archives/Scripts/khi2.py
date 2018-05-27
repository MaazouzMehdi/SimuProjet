import math

def fileTolist () :
	res = []
	fichier = open("valeursHisto.dat", "r")
	for line in fichier :
		res.append(int(line))
	return res
	
	
def khi2 (liste) :
	res = 0
	for i in range(len(liste)) :
		res = res + math.pow((liste[i] - 100000.) / math.sqrt(100000.),2)
	return res

def khi2(liste_occ,liste_theorique) :
	res = 0
	for i in range(len(liste_occ)) :
		res = res + math.pow((liste_occ[i] - liste_theorique[i]) / math.sqrt(liste_theorique[i]),2)
	return res 

if __name__ == "__main__" :
	liste = fileTolist()
	res = khi2(liste)
	print(res)
