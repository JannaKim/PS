import sys; input= lambda: sys.stdin.readline().rstrip()
from math import log

while True:
    L= [*map(int, input().split())]
    if not L[0]:
        break
    # start, ground 필요
    floor= int(log(L[0],2))
    if 2**floor<L[0]:
        floor+=1
    start=2**floor
    ground=start
    mx=ground+L[0]-1

    seg= [0]*2**(floor+1)

    for idx, i in enumerate(range(start,start+L[0])):
        seg[i]=L[idx+1]

    def heapify(k):
        if k>=start:
            return seg[k]
        left= heapify(2*k)
        right= heapify(2*k+1)
        seg[k]= min(left,right)
        return seg[k]
    heapify(1)
    #print(seg)

    def until_ground(k):
        global ground
        if k>=ground:
            return min(ground+L[0]-1,k)
        return until_ground(2*k+1)


    dest=-1
    def heapify_up(lo,hi, left,right,hei): # loc 이후로 hei와 같거나 높은 가장 오늘쪽의 좌표
        global dest
        #print(lo,hi,left,right)
        if lo==left and hi==right:
            if seg[lo//2**int(log(hi-lo+1,2))]>=hei:
                dest= max(until_ground(right),dest)
                return True
        if left==right:
            if seg[left]>=hei:
                dest= max(left,dest)
                return True
            return False
        mid= (lo+hi)//2
        if right<=mid:
            if heapify_up(lo,mid, left,right,hei):
                dest=max(right,dest)
                return True
            return False
        elif mid+1<=left:
            if heapify_up(mid+1,hi, left,right,hei):
                dest=max(right,dest)
                return True
            return False
        else:
            #print('쪼개짐')
            if heapify_up(lo,mid, left,mid,hei):
                if heapify_up(mid+1,hi, mid+1,right,hei):
                    dest=max(right,dest)
                    return True
                dest=max(mid,dest)
            else:
                return False

    ans=0
    for i in range(1,1+L[0]):
        dest=-1
        heapify_up(ground, ground+ground-1, ground+i-1,mx, L[i])
        #print(L[i],dest,'ans',L[i]*(dest-(ground+i-2)))
        ans= max(ans,L[i]*(dest-(ground+i-2)))
    print(ans)

