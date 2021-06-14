n=int(input())
L=[]
for i in range(0,n):
    a= input()
    L.append(a)
q=''
for E in zip(*L):
    for k in range(0,n):
        if E[k]==E[k+1]:
            q+=E[k]
        elif E[k]!=E[k+1]:
            q+='?'
print(q)
        



