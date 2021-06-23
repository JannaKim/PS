t = int(input())
for _ in range(t):
    n = int(input())
    b = bin(n)[2:][::-1]
    m = len(b)
    ans = 0
    for i in range(m):
        if b[i]=='1':
            ans += 3**i
    print(ans)