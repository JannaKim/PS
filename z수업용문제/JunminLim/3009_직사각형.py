
P=[]
for i in range (3):
    a=input()
    P.append(a.split())
Q=[]
R=[]
Ans=[]
print(P)
for i in range (3):
    Q.append(P[i-1][0])
    R.append(P[i-1][1])
for i in range (3):
    for q in range (i+1 , 3 ):
        if Q[i]==Q[q]:
            Ans.append(Q[3-(i+q)])
        
for i in range (3):
    for q in range (i+1 , 3 ):
        if R[i]==R[q]:
            Ans.append(R[3-(i+q)])
            
print(*Ans)
'''
L=[]
for i in range (5):
    L.append(0)
P=[]
for q in range (5):
    P.append(L[::])
P[0][3]='B'

L = list(range(1, 1 +4))
for i in range (4):
    for j in range (i + 1,4):
        for k in range (j + 1,4):
            print(L[i], L[j],L[k])


for i in range (5):
    for j in range(i + 1,5): # nP2
        if i != j:
            print(L[i], L[j])
'''