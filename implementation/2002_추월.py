n = int(input())
dic ={}
for i in range(n):
    dic[input()] = i

L= []
for _ in range(n):
    L.append(dic[input()])

#print(*L)

ans = 0
for i in range(n):
    for j in range(i, n):
        if L[j] < L[i]:
            ans +=1
            break

print(ans)
