a= input()
a= a.split(' ')
L=[]
for i in range(0,int(a[0])):
    b= input()
    L.append(b[::-1])
for k in range(0,int(a[0])):
    print(*L[k],sep='')