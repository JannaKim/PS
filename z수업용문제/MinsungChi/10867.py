a=int(input())
b= (input())
b=b.split(' ')
L=[]
an=[]
for i in range(2002):
    L.append('0')
for l  in range(0,len(b)):
    L[int(b[l])+1000]=1
for h in range(0,len(L)):
    if L[h]==1:
        an.append(h-1000)
print(*an)