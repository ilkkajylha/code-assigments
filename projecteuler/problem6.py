sqrsum = []
sumsqr = []

for i in range(1, 101):
    sumsqr.append(i**2)

for i in range(1, 101):
    sqrsum.append(i)


print sum(sqrsum)**2 - sum(sumsqr)
