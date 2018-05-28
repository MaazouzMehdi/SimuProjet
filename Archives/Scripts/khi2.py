import math

def fileTolist () :
	res = []
	fichier = open("valeursHisto.dat", "r")
	for line in fichier :
		res.append(int(line))
	return res

def getOccurences(decimales) :
	occurrence={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	
	for digit in (decimales) :
		if digit == 0 :
				occurrence[0] +=1
		elif digit == 1 :
			occurrence[1] +=1
		elif digit == 2 :
			occurrence[2] +=1
		elif digit == 3 :
			occurrence[3] +=1
		elif digit == 4 :
			occurrence[4] +=1
		elif digit == 5 :
			occurrence[5] +=1
		elif digit == 6 :
			occurrence[6] +=1
		elif digit == 7 :
			occurrence[7] +=1
		elif digit == 8 :
			occurrence[8] +=1
		else:
			occurrence[9] +=1
	return occurrence
	
def khi2 (liste) :
	res = 0
	for i in range(len(liste)) :
		res = res + math.pow((liste[i] - 100000.) / math.sqrt(100000.),2)
	return res

def compute_Kn(liste_occ,liste_theorique) :
	res = 0
	for i in range(len(liste_occ)) :
		res = res + math.pow((liste_occ[i] - liste_theorique[i]) / math.sqrt(liste_theorique[i]),2)
	return res 
	

if __name__ == "__main__" :
	liste = fileTolist()
	res = khi2(liste)
	print(res)
