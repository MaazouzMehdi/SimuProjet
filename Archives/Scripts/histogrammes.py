from math import *

def prepareToHisto(data) :
	fichier2 = open("valeursHisto.dat","w")
	occurrence={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	
	for i in range(len(data)) :
		if data[i] == 0 :
				occurrence[0] +=1
		elif data[i] == 1 :
			occurrence[1] +=1
		elif data[i] == 2 :
			occurrence[2] +=1
		elif data[i] == 3 :
			occurrence[3] +=1
		elif data[i] == 4 :
			occurrence[4] +=1
		elif data[i] == 5 :
			occurrence[5] +=1
		elif data[i] == 6 :
			occurrence[6] +=1
		elif data[i] == 7 :
			occurrence[7] +=1
		elif data[i] == 8 :
			occurrence[8] +=1
		else:
			occurrence[9] +=1
			
	for key in occurrence :
		fichier2.write(str(occurrence[key]))
		fichier2.write("\n")
	fichier2.close()
