line, row = list(map(int,input().split()))

mp=[]
mp.append(' '*(row+2))
for _ in range(line):
    mp.append(' '+input()+' ')
mp.append(' '*(row+2))


'''
2 4
CAAB
ADCB

3 3
AAC
CAA
ESQ

4 3
JID
ABC
BGF
IHJ
'''

dx = [0,0,1,-1]
dy = [1,-1,0,0]
mx=0

import sys

def f(i,j,cnt):
    global mx
    mx=max(mx,cnt+1)
    if cnt+1==26:
        print(26)
        sys.exit()
    for x,y in zip(dx,dy):
        if mp[i+x][j+y] != ' ' and arr[ord(mp[i+x][j+y])-65]==False:
            # mx = max(mx,sum(1 for value in dic.values() if value==True))
            arr[ord(mp[i+x][j+y])-65]=True
            f(i+x,j+y, cnt+1)
            arr[ord(mp[i+x][j+y])-65]=False

arr = [False]*(91-65)
'''
dic={}
for i in range(65,91):
    dic[chr(i)]=False

dic[mp[1][1]]=True
'''
arr[ord(mp[1][1])-65] = True

f(1,1,0)
print(mx)

'''
12 16
ABCDEFGHIJKLMNOP
BCDEFGHIJKLMNOPQ
CDEFGHIJKLMNOPQR
DEFGHIJKLMNOPQRS
EFGHIJKLMNOPQRST
FGHIJKLMNOPQRSTU
GHIJKLMNOPQRSTUV
HIJKLMNOPQRSTUVW
IJKLMNOPQRSTUVWX
JKLMNOPQRSTUVWXY
KLMNOPQRSTUVWXYZ
LMNOPQRSTUVWXYZA
'''