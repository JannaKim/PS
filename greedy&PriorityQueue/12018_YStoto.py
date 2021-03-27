n, m= map(int, input().split())
L=[]

for _ in range(n):
    num, limit= map(int, input().split())
    ls= [*map(int, input().split())]
    ls.sort(reverse= True)
    if len(ls)<limit:
        L.append(1)
        continue
    L.append(ls[limit-1])

L.sort()
cnt=0
for el in L:
    if el<=m:
        cnt+=1
        m-=el
    else:
        break
print(cnt)

