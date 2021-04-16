import sys; input= lambda: sys.stdin.readline().rstrip()
t= int(input())

s = []

flag = True
def chk(left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            break
    return left >= right

for _ in range(t):
    s= input()
    flag = False
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
           flag = True
           break
    res = left >= right
    if flag:
        res = chk(left + 1, right) or chk(left, right - 1)
    print(2 if not res else int(flag))
