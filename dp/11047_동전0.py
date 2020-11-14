N, K = map(int, input().split())
coin = []
for _  in range(N):
    coin.append(int(input()))

cnt=0
remain = K
idx = 1
while remain:
    a = remain//coin[-idx]
    cnt+=a
    remain -= a*coin[-idx]
    idx+=1

print(cnt)

'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''