n = int(input())
L = [input() for _ in range(n)]
ans=''
for E in zip(*L):
    if len(set(E))==1:
        ans+=E[0]
    else:
        ans+='?'
print(ans)