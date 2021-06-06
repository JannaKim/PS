#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fountainActivation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY locations as parameter.
#

from heapq  import heappop , heappush


def fountainActivation(locations):
    # Write your code here
    n = len(locations)
    fountain = []
    for i in range(n):
        heappush(fountain, ( max(i+1-locations[i] , 1) , -min(i+1+locations[i] , n)) )

    ed = 1
    cnt = 0
    prv = -1
    #print( fountain)
    while fountain:
        lo , hi = heappop(fountain)
        
        hi = -hi
        print(prv)
        #print(lo , hi)
        if lo==ed:
            cnt+=1
            ed = hi + 1
            print(cnt , lo, hi)

        elif ed< lo:
            heappush(fountain , (lo , -hi))
            cnt += 1
            ed = prv + 1


        if prv < hi:
            prv = hi
        #print(ed)
        if ed>n:
            break
        elif prv==n:
            break
    if ed<=n:
        cnt+=1

    return cnt

        
if __name__ == '__main__':