N = int(input())
cow =[-1]*(11)
cnt=0
for _ in range(N):
    a , b = [int(i) for i in input().split()]
    if cow[a]==-1:
        cow[a]=b
    else:
        tmp, cow[a] = cow[a], b
        cnt+=abs(tmp-cow[a])

print(cnt)

# zip(j, j[1:])
'''
8
3 1
3 0
6 0
2 1
4 1
3 0
4 0
3 1
'''