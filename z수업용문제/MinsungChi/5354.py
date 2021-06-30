n= int(input())
L=[]
for i in range(0,n):
    a= int(input())
    for k in range(0,a):
        L.append(['#']*a)
    
    for j in range(1,a-1):
        for f in range(1,a-1):
            L[j][f]='J'
    for m in range(0,a):
        print(*L[m], sep = '')
    print()
    L=[]
    