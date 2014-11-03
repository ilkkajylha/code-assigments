x = 2

def dick(r):
    x = r**2 / 2
    for i in range(1, int(x/2)):
        if x % i == 0: 
            s = i
            t = x/i
            fpair(r, s, t)

def fpair(r, s, t):
    a = s + r
    b = t + r 
    c = r + s + t
    if a<b<c and  a+b+c == 1000:
        print a, " + ",  b, " + ",  c, " = ", a+b+c
        print a*b*c
        return a*b*c


while True:
    dick(x)
    x=x+1    

    
