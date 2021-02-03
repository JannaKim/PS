n, m= map(int, input().split())
a= {}
for _ in range(n):
    a[input()]=1
ans=[]
for _ in range(m):
    b= input()
    if b in a:
        ans.append(b)
print(len(ans))
[print(el) for el in sorted(ans)]