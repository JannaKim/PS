from random import*

L=[]
#random()# 0.0~1.0', 'randint(a,b)', 'shuffle(data)'
for _ in range(5000):
    L.append(randint(-4000, 4000))
    print(L[-1])

L.sort()
print()
print(L[2499])

