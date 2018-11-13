import random

a = [random.randint(1,50) for x in range(random.randint(1,50))]
b = [random.randint(1,50) for x in range(random.randint(1,50))]
c = [x for x in a if x in b]

print(a)
print(b)
print(c)