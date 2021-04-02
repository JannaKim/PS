n,m= map(int, input().split())
lo=1
hi=m

ans=0
for _ in range(int(input())):
    j= int(input())
    if lo<=j and j<=hi:
        continue
    elif j<lo:
        gap= lo-j
        ans+=gap
        lo=j
        hi=lo+m-1
    else:
        gap= j-hi
        ans+=gap
        hi=j
        lo=j-m+1
print(ans)
