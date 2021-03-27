from math import *
ans=[]

a, b= map(int, input().split())

if a**2==b:
    print(-a)
else:
    print(int(-a-sqrt(a**2-b)),int(-a+sqrt(a**2-b)))