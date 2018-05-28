import decimales_recuperator
import khi2
import util
from math import pow
from math import factorial



def compute_Sr(d,occurrences) :
	
	""" Compute the proba to get Sr for all r """
	
	tab = []
	for i in range(1,100) :
		same_size = 0
		S_r = factorial(d) / pow(d,i) * util.stirling(i-1,d-1)
		S_r = S_r * len(occurrences) 
		tab.append(S_r)
	return tab

def create_sequences(decimales) :

	""" Create sequences which contains all digits """
	
	res = []
	sequence = []
	digits = []
	for number in decimales :
		sequence.append(number)
		if number not in digits :
			digits.append(number)
			if len(digits) == 10 :
				res.append(sequence)
				sequence = []
				digits = []
	return res

def caclul_occurrences(sequences) :

	""" Get the occurrences for every sequence which has the same size """
	
	res = []
	same_size=0
	for i in range(10,100 ) :
		same_size=0
		for sequence in sequences :
			if len(sequence) == i :
				same_size += 1
		res.append(same_size)
	return res

if __name__ == "__main__":
	occurrences = create_sequences()

	tab = compute_Sr(10,occurrences)
	tab = tab[9::]
	
	moi = count_occurrences(occurrences)
	
	value = khi2.khi2(moi,tab)
	print(value)
	#print(tab)
