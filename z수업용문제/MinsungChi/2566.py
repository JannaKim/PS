L=[]
for i in range(0,9):
    L.append(list(map(int, input().split(' '))))
d=0

for g in range(0,9):
    for h in range(0,9):
        if L[g][h]>d:
            d = L[g][h]
print(d)
for g in range(0,9):
    for h in range(0,9):
        if d==L[g][h]:
            print(g+1)
            print(h+1)