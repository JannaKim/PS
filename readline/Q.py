'''
from sys import *
for L in stdin:
    print(sum([int(i) for i in L.split()]))

'''
print(list(map(lambda x:3*x, [1,2,3,4])))

T1 = ("a", "b", "c")
T2 = (1,2,3)
T3 = (4,'d')
print(T1[2], T2[1])
T1=T1+T3
print(T1[2:5])
print(T3*T2[1])