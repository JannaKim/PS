'''
from functools import cmp_to_key as cmp
def f(a,b):
    if a[0]==b[0]:
        return b[1]-a[1]
    else:
        return a[0]-b[0]

s= input()
n= len(s)
if n==3:
    print(s)
    exit()
L=[]
for i in range(n):
    L.append((ord(s[i]),i))
L.sort(key= cmp(f))

#print(L)
idx=0
a= L[idx][1]
while a>=n-2:
    idx+=1
    a= L[idx][1]
#print(a)
L=[]
for i in range(a+1,n):
    L.append((ord(s[i]),i))
L.sort(key= cmp(f))
idx=0
b= L[idx][1]
#print(L)
while b==n-1:
    idx+=1
    b= L[idx][1]
#print(a,b)
print(s[a::-1],end='')
print(s[b:a:-1],end='')
print(s[:b:-1])
'''



s= input()
n= len(s)
ans='z'*n
for a in range(n-2):
    for b in range(a+1,n-1):
        tmp=s[a::-1]+s[b:a:-1]+s[:b:-1]
        if tmp<ans:
            ans=tmp
print(ans)
