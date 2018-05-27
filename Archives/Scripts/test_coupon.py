import decimales_recuperator
from sympy.functions.combinatorial.numbers import stirling
import khi2
from math import pow
from math import factorial



def calculS_r(d,occurrences) :
	tab = []
	for i in range(1,100) :
		same_size = 0
		S_r = factorial(d) / pow(d,i) * stirling(i-1,d-1)
		S_r = S_r * len(occurrences) 
		tab.append(S_r)
	return tab

def count_occurrence() :
	data = decimales_recuperator.toData()
	res = []
	sequence = []
	digits = []
	for i in data :
		sequence.append(i)
		if i not in digits :
			digits.append(i)
			if len(digits) == 10 :
				res.append(sequence)
				sequence = []
				digits = []
	return res

def count(occ) :
	res = []
	same_size=0
	for i in range(10,100 ) :
		same_size=0
		for sequence in occ :
			if len(sequence) == i :
				same_size += 1
		res.append(same_size)
	return res

if __name__ == "__main__":
	occurrences = count_occurrence()

	tab = calculS_r(10,occurrences)
	tab = tab[9::]
	
	moi = count(occurrences)
	
	value = khi2.khi2(moi,tab)
	print(value)
	#print(tab)
