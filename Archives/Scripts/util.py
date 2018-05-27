import math

def calculate_histo(list):
    occur=[0]*10
    for i in range(len(list)):
        if list[i]<0.1:
            occur[0]+=1
        elif list[i]<0.2:
            occur[1]+=1
        elif list[i]<0.3:
            occur[2]+=1
        elif list[i]<0.4:
            occur[3]+=1
        elif list[i]<0.5:
            occur[4]+=1
        elif list[i]<0.6:
            occur[5]+=1
        elif list[i]<0.7:
            occur[6]+=1
        elif list[i]<0.8:
            occur[7]+=1
        elif list[i]<0.9:
            occur[8]+=1
        else:
            occur[9]+=1
    return occur

def binomial(n, k) :
  return math.factorial(n) / math.factorial(k) / math.factorial(n-k)

def stirling(k, r) :
    return sum((-1)**(r-i)*binomial(r, i)*i**k for i in range(r+1)) / math.factorial(r)