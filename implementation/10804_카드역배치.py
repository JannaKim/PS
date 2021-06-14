L = list(range(1,  21))
for _ in range(10):
    a , b = [int(i) - 1 for i in input().split()]
    #print(b , a-1, L[a:b + 1] , L[b: -2:-1])
    if not a:
        L = L[b::-1] + L[b+1:]
    else:
        L[a:b + 1] = L[b: a - 1:-1]
    #print(L)
    
print(*L)