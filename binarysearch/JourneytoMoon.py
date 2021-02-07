n, p= map(int, input().split())
L=[[]]
a, b= map(int, input().split())
L[0].append(a)
L[0].append(b)
for _ in range(p-1):
    a, b= map(int, input().split())
    for g in L:
        if BS(a, g):
            dic[k]
        BS