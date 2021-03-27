from heapq import heappush, heappop
# 비싼걸 작은 가방부터
n, k= map(int, input().split())
L=[]
for _ in range(n):
    w, v= map(int, input().split())
    L.append((w, v))
L.sort(reverse= True) # 무거운 순

bag= [int(input()) for _ in range(k)]
bag.sort() # 작은 크기 가방순으로 

jew= []
ans=0
for el in bag: # 가방 가벼운 순
    while L and L[-1][0]<=el:
        w, v= L.pop()
        heappush(jew, (-v))
    if not jew:
        continue
    ans+=-heappop(jew)
print(ans)


'''
7 5
2 100
11 100
12 100
10 101
10 1
10 0
10 50
1
2
10
10
10

5 5
9 5
4 4
1 3
11 2
1 1
2
3
4
10
10
'''