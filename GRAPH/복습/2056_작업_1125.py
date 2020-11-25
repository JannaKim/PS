# 현재 작업을 위해 필요한 정보가 이전에 모두 주어지므로, 
# 바로 연결돼있는 노드의 최대 시간만 가져와서 자신과 더하면 된다

N = int(input())
edge = [[]for _ in range(N+1)]
time = [0]*(N+1)
for i in range(1,N+1):
    *L,=map(int, input().split())
    time[i]=L[0]

    for v2 in L[2:]:
        edge[i].append(v2)

total = time[:]
total[1]=time[1]
for i in range(2,N+1):
    for v2 in edge[i]:
        total[i]=max(total[i], total[v2]+time[i])

print(max(total))


'''
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6
'''


'''
The necessary info to define accum[v] is always perfectly defined before the attempt to define accum[v].
'''