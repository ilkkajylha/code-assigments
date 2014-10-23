primelist = [2, 3, 5, 7, 11]
x = 13

def isnotprime(x):    
    for i in range(2, x):
        if (x % i) == 0:
            break
    else:
        primelist.append(x)

        
while len(primelist) <= 10000:
    isnotprime(x)
    x+=1
print primelist[10000]
