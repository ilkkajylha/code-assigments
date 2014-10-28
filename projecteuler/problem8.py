numbers = []
sums = []
x = 0
y = 13
z = 1 
with open('problem8.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        numbers.append(c)

numbers.remove('\n')
numbers = map(int, numbers)
while True:
    for i in numbers[x:y]: 
            z = z * i
    sums.append(z)
    x, y, z = x+1, y+1, 1 
    if y > len(numbers):
        break

print max(sums)
