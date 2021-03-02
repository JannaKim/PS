n= int(input())
chk=[False]*n
L=[*map(int, input().split())]
def stamp(k,cnt):
    #print(k,cnt)
    if not chk[k+L[k]] and 0<=k+L[k] and k+L[k]<n:
        chk[k+L[k]]= True
        return stamp(k+L[k],cnt+1)
    else:
        return cnt+1

ans=-1
for i in range(3):
    chk=[False]*n
    ans=max(stamp(i,1),ans)
print(ans)


'''
10
3 5 -1 -2 4 4 3 -2 -3 -2
'''