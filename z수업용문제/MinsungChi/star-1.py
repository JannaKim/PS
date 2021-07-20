L=[]
a= int(input())
for k in range(0, a):
    L.append([' ']*a)
    
for i in range(a):
    for j in range(a - 1 - i, a):
        
        L[i][j] = '*'

for s in range(0,a):
    print(*L[s], sep = '')