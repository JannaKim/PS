t = int(input())
for a in range(t):
    n, x = map(int,input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    A.sort()
    B.sort(reverse=True)
    ans = True
    for i in range(n):
        if A[i]+B[i]<=x:
            continue
        else:
            ans=False
            break
    if ans ==True:
        print('Yes')
    else:
        print('No')
    if a!=t-1:
        blank=input()

