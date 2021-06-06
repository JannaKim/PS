#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'encryptionValidity' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER instructionCount
#  2. INTEGER validityPeriod
#  3. INTEGER_ARRAY keys
#
def encryptionValidity(instructionCount, validityPeriod, keys , n):
    # Write your code here
    keys.sort()

    encryptionCnt = -1
    e= 100000
    net= [True]*(e+1)
    for i in range(2,int(e**(0.5))+1):
        if net[i]:
            for j in range(2*i, e+1, i):
                net[j]=False
    net[2] = False
    chk = [False] * n
    def dfs(idx):
        sm  = 1
        for i in range(idx-1 , -1 , -1):
            if net[keys[i]]:
                continue
            if not chk[i] and not keys[idx] % keys[i]:
                chk[i] = True
                sm += dfs(i)
        return sm


    encryptionCnt = 1
    for i in range(n):
        
        chk = [False] * n
        amount = dfs(i)
        encryptionCnt =  max(encryptionCnt, amount)

            
    if instructionCount>validityPeriod:
        instructionCount = float(instructionCount)/( 10 ** 5 )
    else:
        validityPeriod = float(validityPeriod)/( 10 ** 5 )

    valid = instructionCount * validityPeriod
    #print(valid)
    if valid >= encryptionCnt:
        return [1 , encryptionCnt * (10 ** 5)]
    else:
        return [0 , encryptionCnt * (10 ** 5)]

            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    instructionCount = int(input().strip())

    validityPeriod = int(input().strip())

    keys_count = int(input().strip())

    keys = []

    for _ in range(keys_count):
        keys_item = int(input().strip())
        keys.append(keys_item)

    result = encryptionValidity(instructionCount, validityPeriod, keys , keys_count)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
