result = []
a, b, = 1, 1  
while b < 4000000:
    if b % 2 == 0:
        result.append(b)
    a, b = b, a+b

print sum(result)
