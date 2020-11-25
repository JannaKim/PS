from sys import *
input = lambda: stdin.readline().rstrip()

n = int(input())
seq = [int(input()) for _ in range(n)]

Q=[]
num=0
ans=[]

while seq:
    if not Q:
        ans.append('+')
        num+=1
        Q.append(num)
    last = Q.pop()
    if last<seq[0]:
        Q.append(last)

        ans.append('+')
        num+=1
        Q.append(num)

    elif last==seq[0]:
        ans.append('-')
        seq.pop(0)

    
    else: # last>seq
        print('NO')
        exit()

[print(i) for i in ans]


