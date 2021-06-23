a= int(input())
L=[0]*a

M=[]
N=[]
j=0
l=0
n= int(input())
for k in range(0,n):
    b= input()
    b=b.split()
    c= (int(b[1])-int(b[0]))+1
    M.append(c)
    for  t in range(int(b[0])-1,int(b[1])):
        if L[t] == 0:
            L[t]=1
            l+=1
        
    N.append(l)
    l=0

    j +=1

for h in range(0,len(M)):
    if max(M)==M[h]:
        print(h+1)
        break

for d in range(0,len(N)):
    if max(N)==N[d]:
        print(d+1)
        break

