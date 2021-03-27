import sys; input= lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n= int(input())
    L=[*map(int, input().split())]
    plus=[]
    L.sort()
    A=set()
    for a, b in zip(L,L[1:]):
        A.add(a)
        if a==b:
            plus.append(b)
    if n==1:
        A.add(L[0])
    else:
        A.add(L[-1])
    A=list(A)
    print(*(A+sorted(plus)))

    

