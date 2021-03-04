from heapq import heappush, heappop
from bisect import bisect_left as bs
# 비싼걸 작은 가방부터
n, k= map(int, input().split())
jew= []
for _ in range(n):
    w, v= map(int, input().split())
    heappush(jew, (-v, -w))

bag= [int(input()) for _ in range(k)]
chk= [False]*k



# bisect


#bisect.bisect_left(a, x, lo=0, hi=len(a))
#정렬된 순서를 유지하도록 a에 x를 삽입할 위치를 찾습니다. 매개 변수 lo 와 hi는 고려해야 할 리스트의 부분집합을 지정하는 데 사용될 수 있습니다; 기본적으로 전체 리스트가 사용됩니다. x가 a에 이미 있으면, 삽입 위치는 기존 항목 앞(왼쪽)이 됩니다. 반환 값은 a가 이미 정렬되었다고 가정할 때 list.insert()의 첫 번째 매개 변수로 사용하기에 적합합니다.

#반환된 삽입 위치 i는 배열 a를 이분하여, 왼쪽은 all(val < x for val in a[lo:i]), 오른쪽은 all(val >= x for val in a[i:hi])이 되도록 만듭니다.
ans=0
unfilled=k
while jew:
    val, wei= heappop(jew)
    val=-val
    wei=-wei
    loc= bs(bag, wei,0,k)# wei넣을 수 있는 가장 작은 가방의 인덱스 가져옴
    if loc==k:
        continue

    if not chk[loc]:
        chk[loc]=True
        ans+=val
        unfilled-=1
        #print(chk)
    else:
        tmp=loc
        while chk[tmp] and tmp<k:
            tmp+=1
        #print(tmp)
        if tmp==k:
            continue
        else:
            unfilled-=1
            ans+=val
            #다 밀고 새로운 애 집어넣음
            chk[tmp]=True
        #print(chk)
    if not unfilled:
        print(ans)
        exit()
print(ans)
        



