n = int(input())

H = [0] * n
q = []
for i in range(n):
    ths = int(input())
    while q:
        if q[-1][0] > ths:
            break
        else:
            q.pop()
    q.append( (ths, i))
    H[i] = len(q) - 1
print(sum(H))