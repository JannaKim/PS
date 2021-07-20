L = []
for i in range(0, 9):
    i = int(input())
    L.append(i)
mx = 0
idx = 0
for i in range(0, len(L)):
    if L[i] > mx:
        mx = L[i]
        idx = i + 1
print(mx)
print(idx)