n = int(input())
L= [*map(int, input().split())]

def find():
    a, b = -1, -1
    for i in range(1,11):
        if H[i]:
            a = i
            break
    for i in range(10, 0, -1):
        if H[i]:
            b = i
            break
    return (a, b)

ans = 0
H = [0]*11
H[L[0]]+=1

lo = 0
hi = 0

ans = 0
while lo <= hi and hi < n:
    mn, mx = find()
    if mx - mn <= 2:
        ans = max(ans, hi-lo + 1)
        hi +=1
        if hi == n:
            break
        H[L[hi]]+=1
    else:
        H[L[lo]]-=1
        lo +=1
print(ans)

'''
10
1 2 3 4 5 4 3 2 1 2
'''