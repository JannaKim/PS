n= int(input())
L=[*map(int, input().split())]
'''
L.sort()
s=  0

if sum(L)!=n*(n-1)//2:
    print(-1)
    exit()
for i in range(n):
    s+=L[i]
    if s<(i+1)*i//2:
        print(-1)
        exit()
print(1)

'''
L.sort(reverse=True)
cnt= [0]*n
if sum(L)!=n*(n-1)//2:
    print(-1)
    exit()
for i in range(n):
    cnt[L[i]]+=1

for idx,i in enumerate(range(n-1,-1,-1)):
    if cnt[i]>idx+1:
        print('?')
        print(-1)
        exit()
print(1)

# 한명 