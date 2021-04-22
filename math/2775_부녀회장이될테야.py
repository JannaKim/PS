from math import factorial as fac
import sys; input= lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n= int(input())+1
    r= int(input())
    print(fac(n+r-1)//(fac(r-1)*fac(n)))