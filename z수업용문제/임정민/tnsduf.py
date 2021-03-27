'''
n=int(input())
chk=[False]*n
q=[]
def f(i):
    print(q)
    if len(q)==n:
        print(*q)
        return
    for j in range(n):
        if j+1 not in q: 
            q.append(j+1)
            f(j)
            q.remove(j+1)
f(n)
'''
'''
n= int(input())
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            #print(i,j,k)
            if len({i,j,k})==3:
                print('ㅡㅡㅡ',i,j,k)
'''
while True:
    L = [*map(int, input().split())]
    if L[0]==0:
        break
    M= L[1:][:]
    n=len(M)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    for m in range(l+1,n):
                        for o in range(m+1,n):
                            print(M[i],M[j],M[k],M[l],M[m],M[o])
    print()