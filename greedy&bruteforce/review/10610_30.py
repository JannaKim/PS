import sys; input= lambda: sys.stdin.readline().rstrip()
L= list(input())
L.sort(reverse=True)
if L[-1]=='0' and int(''.join(L[:-1]))%3==0:
    print(''.join(L))
else:
    print(-1)