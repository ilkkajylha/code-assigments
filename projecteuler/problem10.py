import math
primelist = []
x = 2

def isnotprime(x):    
    for i in range(2, int(math.sqrt(x) + 1)):
        if (x % i) == 0:
            break
    else:
        primelist.append(x)

        
while x < 2000000:
    if math.sqrt(x) != 0:
        isnotprime(x)
    x+=1
print sum(primelist)
