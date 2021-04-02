n= int(input())
L=[0]
for _ in range(n):
    L.append(int(input()))
L.append(0)
stk=[(0,0)]
ans= L[0]
for i in range(1, n + 2):
    while stk[-1][0]>L[i]: # 작으면 길이 다 비교
        h = stk[-1][0]
        stk.pop()
        ans= max(ans,(i-stk[-1][1]-1)*h ) # pop한 후 마지막 
            
            
    stk.append((L[i], i))
    
print(ans)