# 시간초과
N, C = map(int, input().split())
dic={}
*L, = map(int, input().split())
CNT = [[] for _ in range(N+1)]
for i in range(1,C+1):
    CNT[L.count(i)].append(i)

ans = []
for idx in range(N,0,-1):
    if not CNT[idx]:
        continue
    elif len(CNT[idx])==1:
        [ans.append(*CNT[idx]) for _ in range(idx)]
    else:
        CNT[idx].sort(key = lambda x: L.index(x))
        for el in CNT[idx]:
            [ans.append(el) for _ in range(idx)]
print(*ans)

'''
6 2
2 2 2 1 1 1

5 2
2 1 2 1 2
'''




