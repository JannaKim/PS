import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())
L=[]
for _ in range(n):
    L.append(int(input()))

L.sort()
if sum(L)/n>=0:
    print(int(sum(L)/n+0.5))
else:
    print(int(sum(L)/n-0.5))


mid= (n-1)//2
print(L[mid])
chk=[0]*8002
for el in L:
    chk[el+4000]+=1

mx=0
ans=0
second=False
for i in range(8002):
    if chk[i]>mx:
        #print(i)
        mx=chk[i]
        second=False
        ans=i-4000
    elif chk[i]==mx:
        #print(i)
        if not second:
            ans=i-4000
            second=True
print(ans)
print(L[-1]-L[0])


'''
7
1
2
3
4
4
5
5

3
4
5
4
'''