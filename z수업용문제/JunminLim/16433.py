n,r,c=map(int, input().split())
Q=[]
for i in range (n):
    Q.append([0]*n)
for i in range (n):
    for j in range (n):
        if (abs(i-r)+abs(c-j))%2==0:
            Q[i][j]='v'
        else:
            Q[i][j]='.'
for i in Q:
    print(*i,s='')