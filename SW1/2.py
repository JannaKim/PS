p, n, h= map(int, input().split())

edge= [[] for _ in range(n+1)]
for _ in range(n):
    a, b= map(int, input().split())
    edge[a].append(b)


for i in range(1,p+1):
    dp=[1]+[0]*h
    for el in edge[i]:
        for j in range(h+1):
            if dp[j] and j+el<=h:
                dp[j+el]=1
    for i in range(h, -1,-1):
        if dp[i]:
            print(i*1000)
            break

'''
2 7 4
1 10
1 5
1 7
2 10
2 1
2 3
2 7

1 4 11
1 5
1 4
1 3
1 3
'''