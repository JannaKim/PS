n, m= map(int, input().split())
xheard=set()
xseen=set()
for _ in range(n):
    xheard.add(input())
for _ in range(m):
    xseen.add(input())

ans= sorted(list(xheard & xseen))
print(len(ans))
[print(el) for el in ans]
