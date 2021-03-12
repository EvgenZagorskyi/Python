import random
a = random.randrange(10000, 99999)
a1 = a // 1 % 10
a2 = a // 10 % 10
a3 = a // 100 % 10
a4 = a // 1000 % 10
a5 = a // 10000 % 10
a6 = a1 + a2 + a3 + a4 + a5
print(a)
print(a6)