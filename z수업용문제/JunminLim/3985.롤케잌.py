l=int(input())
n=int(input())
L=[]
mx=-1
PKsave=[]
for i in range (n):
    p,k=map(int, input().split())
    L.append((k-p))
    PKsave.append((p,k))
    if mx<k-p:
        mx=k-p
        exp_aud=i+1

t=[0]*l
#t=롤케익
for left, right in PKsave:
    for q in range(left, right+1):
        print(q)
        t[q-1]=1
print(t)
print(q)
#print(exp_aud,)

