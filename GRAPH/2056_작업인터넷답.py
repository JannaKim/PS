from time import*
import sys
start = time()
#sys.stdin = open('test3.txt', 'r')

n = int(input())
times = [0] * (n+1)
graph = {}
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    times[i] = lst[0]
    if lst[1] == 0:
        continue
    for j in lst[2:]:
        if i in graph:
            graph[i].append(j)
        else:
            graph[i] = [j]
            
for i in range(1, n+1):
    if i in graph:
        T = 0
        for j in graph[i]:
            T = max(T, times[j])
        times[i] += T
        print(f'times[{i}]={times[i]}')
        
print(max(times))

print("time :", time() - start)

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