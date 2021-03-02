for _ in range(int(input())):
    n = int(input())
    C= input().split()
    ans=C[0]
    for i in range(1,n):
        if ord(C[i])<=ord(ans[0]):
            ans= C[i]+ans
        else:
            ans+=C[i]
    print(ans)