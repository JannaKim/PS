r = range
n= int(input())
L= [int(input()) for _ in r(n)]
L.sort()


n,*l=map(int,open(0));print(max(j+j*(n:=n-1)for j in sorted(l)))
mx=0
for i in r(n):
    mx= max(L[i]*(n-i), mx)
print(mx)