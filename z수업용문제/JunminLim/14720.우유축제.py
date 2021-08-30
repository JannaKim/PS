#딸초바딸->
n=int(input())
L = list(map(int, input().split()))
goal=0
g=0
for i in range(n):
    if L[i]==g:
        goal+=1
        g = (g + 1) % 3

print(goal)


# 0 1 2 0 1 2