n= int(input())
L=[*map(int, input().split())]
L.sort()
left=0
right=n-1
ans=1e9*100000
prnt=[L[left],L[left+1]]
while left<n:
    #print(left,right)
    if left>=right:
        right+=1
        continue
    if right<n and ans>abs(L[left]+L[right]):
        ans=abs(L[left]+L[right])
        prnt=[L[left],L[right]]
    if right<n and left+1<right and abs(L[left]+L[right-1])<abs(L[left]+L[right]):
        while left+1<right and abs(L[left]+L[right-1])<abs(L[left]+L[right]):
            right-=1
            if ans>abs(L[left]+L[right]):
                ans=abs(L[left]+L[right])
                prnt=[L[left],L[right]]
    else:
        while right<n-1 and abs(L[left]+L[right+1])<abs(L[left]+L[right]):
            right+=1
            if ans>abs(L[left]+L[right]):
                ans=abs(L[left]+L[right])
                prnt=[L[left],L[right]]
    left+=1

print(*prnt)
    
'''
7
-99 -2 -1 1 98 100 101
'''