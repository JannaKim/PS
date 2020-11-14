N = int(input())
S, K = [int(i) for i in input().split()]
L = [int(i) for i in input().split()]

score = []
for i in range(N):
    score.append((L[i], i+1))

score.sort(key= lambda x: S-x[0] if S>=x[0] else x[0]-S+0.1)

[print(idx,end=' ') for (sc,idx) in score[:K]]
'''
5
60 3
20 80 100 40 10
'''