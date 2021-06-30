gap = 1e10
ans = [-1, -1]

n = int(input())
L = [*map(int, input().split())]
lo = 0
hi = n - 1
while lo < hi:
    tmp = abs(L[lo] + L[hi])
    if gap > tmp:
        gap = tmp
        ans = [L[lo], L[hi]]
    if L[lo] + L[hi]>=0: # 양수면 오른쪽을 줄임
        hi -= 1

    else:
        lo += 1
    
    
print(*ans)