result = []
x, i = 600851475143, 2 
while i <= x:     
    if x % i != 0:
        i=i+1
    elif x % i == 0:
        result.append(i)
        x = x / i
        i = 2

print max(result)
