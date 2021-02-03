import sys; input= lambda: sys.stdin.readline().rstrip()
k= int(input())
q=[]
for _ in range(k):
    a= int(input())
    if a:
        q.append(a)
    else:
        q.pop()
print(sum(q))