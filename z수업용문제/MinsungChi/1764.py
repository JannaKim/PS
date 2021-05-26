a=input()
a= a.split(' ')
d={}
dic={}
L=[]
Li=[]
for i in range(0,int(a[0])):
    b=input()
    L.append(b)
    d[b]=i
for t in range(0,int(a[1])):
    b=input()
    dic[b]=i
    L.append(b)
for h in range(0,len(L)):
    if L[h]in d and L[h]in dic:
        Li.append(L[h])
print(len(Li)//2)
Li= set(Li)
Li= sorted(Li)
for g in range(0,len(Li)):
    print(Li[g])