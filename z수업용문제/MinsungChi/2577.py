a= int(input())
b= int(input())
c= int(input())
d= a*b*c
d= str(d)
L=[]
for i in range(0,10):
    L.append(0)
for h in range(len(d)):
    tmp= int(d[h])
    L[tmp]+=1
print(*L, sep='\n')