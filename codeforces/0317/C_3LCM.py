import sys; input= lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n, k= map(int, input().split())
    half=n//2
    if not n%2 and not half%2:
        print(half, half//2, half//2)
    
    elif not n%2 and half%2:
        half-=1
        print(half,half,2)
    else:
        print(half, half, 1)