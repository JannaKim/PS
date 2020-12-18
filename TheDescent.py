import sys
import math




while True:
    L=[]
    j=0
    for i in range(8):
        mountain_h = int(input())
        L.append(mountain_h)
    j= max(L)
    for k in range(0,len(L)):
        if L[k]==j:
            print(k)
    #j=0
   # L=[]
'''
import sys
import math
while True:
    L = []
    for i in range(8):
        mountain_h = int(input())
        L.append(mountain_h)
    print(L.index(max(L)))
'''