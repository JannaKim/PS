n, k=map(int, input().split())
won=[int(input()) for _ in range(n)]
won.sort(reverse=True)

mn=1e15
def zeroone(i, ans, cst):
    #print(i,ans,cst)
    if i==n:
        global mn
        mn=min(mn, ans+cst)
        return

    #if i+1<leng and won[i]/2.5==won[i+1]:
    zeroone(i+1, ans,cst)
    ans+=cst//won[i]
    cst=cst%won[i]   
    zeroone(i+1, ans, cst)


zeroone(0,0,k)
print(int(mn))