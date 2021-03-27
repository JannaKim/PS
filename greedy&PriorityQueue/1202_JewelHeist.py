from heapq import heappush, heappop
from collections import deque
# 비싼걸 작은 가방부터
n, k= map(int, input().split())
jew= []
for _ in range(n):
    w, v= map(int, input().split())
    heappush(jew, (-v, -w)) # 가치 큰 순으로. 무거운순으로

bag= [int(input()) for _ in range(k)]
bag.sort() # 작은 크기 가방순으로 
# bisect


#bisect.bisect_left(a, x, lo=0, hi=len(a))
#정렬된 순서를 유지하도록 a에 x를 삽입할 위치를 찾습니다. 매개 변수 lo 와 hi는 고려해야 할 리스트의 부분집합을 지정하는 데 사용될 수 있습니다; 기본적으로 전체 리스트가 사용됩니다. x가 a에 이미 있으면, 삽입 위치는 기존 항목 앞(왼쪽)이 됩니다. 반환 값은 a가 이미 정렬되었다고 가정할 때 list.insert()의 첫 번째 매개 변수로 사용하기에 적합합니다.

#반환된 삽입 위치 i는 배열 a를 이분하여, 왼쪽은 all(val < x for val in a[lo:i]), 오른쪽은 all(val >= x for val in a[i:hi])이 되도록 만듭니다.

def bs(L,weight):

    lo=0
    hi= k-1
    answer=-1
    while lo<=hi:
        m=(lo+hi)//2
        if L[m]>=weight: #답이 될 수 있다
            answer=m
            hi=m-1
        else:
            lo=m+1
    return answer

ans=0
unfilled=k # 가방의 개수. 하나 채울때마다 -1해준다.
empty=k-1 #큰 가방부터 채운다
miniwei=1e9
minilocs=[]
while unfilled and empty>=0:
    if not jew:
        break
    val, wei= heappop(jew)
    val=-val # 큰순으로 가치 가져왔음
    wei=-wei
    #print(val,wei)
    
    loc= bs(bag,wei)# wei넣을 수 있는 가장 작은 가방의 인덱스 가져옴
    if loc==-1: # 가방이 무게보다 작으면 못넣고 지나감
        continue
    if loc<=empty: # 만약 안 차 있으면 그냥 집어넣음
        empty-=1
        ans+=val
        unfilled-=1
        if miniwei>wei:
            miniwei=wei
            minilocs=[]
            heappush(minilocs,empty+1)
        elif miniwei==wei:
            heappush(minilocs,empty+1)

    else:# 차 있다면
        #print(f'{bag[empty]}>={wei} and {miniwei}>={bag[empty]}')
        passed=[]
        while minilocs:
            idx= heappop(minilocs)
            if miniwei<=bag[empty] and wei<=bag[idx]: # 가장 가벼운 애가 있는 맨 왼쪽 위치랑랑 자리 바꾸는셈 치면
                ans+=val
                heappush(minilocs, empty)
                empty-=1
                unfilled-=1
                miniwei= min(miniwei,wei)
                for el in passed:
                    heappush(minilocs,el)
                    passed=[]
                break
            else:
                passed.append(idx)
            if miniwei>wei:
                miniwei=wei
                minilocs=[]
                heappush(minilocs,empty+1)
            elif miniwei==wei:
                heappush(minilocs,empty+1)
        for el in passed:
            heappush(minilocs,el)
    #print('ans',ans)
print(ans)

#print(bs(11))

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
10 2
1 1
2
3
4
10
10
'''