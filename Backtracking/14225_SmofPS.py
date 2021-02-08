n= int(input())
L= [*map(int, input().split())]
dp= [0]*(100000*20+1)
for el in L:
    for i in range(100000*20, -1, -1):
        if i==0 or dp[i]:
            dp[i+el]=1
i=1
while dp[i]:
    i+=1
print(i)