from bisect import bisect_left, bisect_right
n, h= map(int, input().split())
d=[]
ru=[]
for _ in range(n//2):
    d.append(int(input()))
    ru.append(h-int(input()))
d.sort()
ru.sort()
def crash(k):
    return n//2-bisect_left(d,k) + bisect_right(ru,k-1)
    

ans=1e9
nm=0
for i in range(1,h+1):
    if ans >crash(i):
        nm=1
        ans=crash(i)
    elif ans==crash(i):
        nm+=1

print(ans,nm)
'''
4 10
1
8
1 
8
'''