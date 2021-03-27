import sys; input= lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n, k1, k2= map(int, input().split())
    w, b= map(int, input().split())

    a, c= k1, k2
    w-=min(a,c)
    w-=abs(a-c)//2

    a, c= n-k1, n-k2
    b-=min(a,c)
    b-=abs(a-c)//2

    if w<=0 and b<=0:
        print('YES')
    else:
        print('NO')
