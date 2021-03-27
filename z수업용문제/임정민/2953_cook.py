l=[]
L=[]
for i in range (5):

    a,b,c,d=map(int,input().split())
    p=a+b+c+d
    l.append(p)
for x in range (5):
    L.append((l[x],x+1))
L.sort()
print(*L[4][::-1])