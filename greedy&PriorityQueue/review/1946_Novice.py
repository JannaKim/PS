import sys; input= lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n= int(input())
    q=[]
    for _ in range(n):
        a, b= map(int, input().split())
        q.append((a,b))
    q.sort()
    rank=1e9
    cnt=0
    for a, b in q:
        if b<rank:
            rank=b
            cnt+=1
    print(cnt)