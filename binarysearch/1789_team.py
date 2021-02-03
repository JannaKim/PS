import sys
input=sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))
left = 0 
right = max(a) #20
ans = 0
while(right>=left):
    if(right-left<=1):
        cut = 0
        for i in range(N):
            if right <= a[i]:
                cut += a[i]-right
        if(cut>=M):
            ans = right
            break
        else:
            ans = left
            break
    mid = (left+right)//2 #10, 11, 12, 13, 14 // right=19 mid=23//2=11
    cut = 0
    for i in range(N):
        if mid <= a[i]:
            cut += a[i]-mid #cut=(0+5+7+10)=22, 22-4=18, 18-4=14, 14-4=10, 10-4=6, //x+4+3+9=16
    if(cut>=M):
        if(ans<mid):
            ans = mid
        left = mid
    else:
        right = (mid-1)
print(ans)