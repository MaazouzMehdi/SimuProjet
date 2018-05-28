
def getDecimales() :

	""" get decimales of pi from a file and put them in a list """
	
	fichier = open("../Enonce/pi6.txt", "r")
	res = []
	firstLine = True
	for line in fichier :
		if firstLine :
			firstLine = False
			continue
			
		for i in range(len(line)) :
			if line[i]!="\n" :
				res.append(int(line[i]))
	fichier.close()
	return res

if __name__ == "__main__":
	all_decimales = getDecimales()

