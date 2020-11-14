# 메모리초과
X, A, B, C, D = map(int, input().split())

# 이따 로그로 바꾸기
bag = [] # (금액, 개수, 쓴 동전)
def binary_pack(am, v, X): # amount, val, X
    pw = len(bin(am)[2:])
    while am:
        if am == 2**pw-1:
            for i in range(pw):
                bag.append([v*(2**i), 2**i, X])
            break
        else:
            for i in range(pw-1):
                bag.append([v*(2**i), 2**i, X])
            am = am-2**(pw-1)+1
            pw = len(bin(am)[2:])
binary_pack(A, 1, 0)
binary_pack(B, 5, 1)
binary_pack(C, 10, 2)
binary_pack(D, 25, 3)
#[print(bag[i],end= (' ' if (i+1)%10 else '\n' )) for i in range(len(bag))]

#dp[i][j][0]: 0~i번째 동전까지 내서 j원을 맞출 때 낼 수 있는 최대 동전 개수
#dp[i][j][1]: 사용한 동전별 개수 [penny, dime, nickle, quarter]
dp=[]
for i in range(len(bag)):
    dp.append([])
    [dp[i].append([]) for _ in range(X+1)]
    for j in range(X+1):
        dp[i][j] = [0,[0,0,0,0]]

Len_Of_bag = len(bag)
for i in range(Len_Of_bag):
    for j in range(X+1):
        #print(' ',i,j)
        if bag[i][0]==j: # 동전 하나로 값 j가 채워진 게
            if bag[i][1]>dp[i-1][j][0]: # 현재 dp보다 더 많은 동전을 내는 거라면
                dp[i][j][0] = bag[i][0]

                a = [0,0,0,0]
                a[bag[i][2]]+=bag[i][1] #쓴 동전의 인덱스에 해당하는 곳에 개수 더하기
                dp[i][j][1] = a
            else:
                dp[i][j] = dp[i-1][j][:] 


        elif bag[i][0]<j:
            if dp[i-1][j-bag[i][0]][0] !=0 and dp[i-1][j-bag[i][0]][0] + bag[i][1] > dp[i-1][j][0]: # 더 많은 동전 낼 수 있다면
                    dp[i][j][0] = dp[i-1][j-bag[i][0]][0] + bag[i][1]
                    a = [0,0,0,0]
                    a[bag[i][2]]+=bag[i][1] # 현재 받은 동전에 해당되는 개수

                    for idx,k in enumerate(dp[i-1][j-bag[i][0]][1]):
                        a[idx]+=k
                    
                    dp[i][j][1] = a                
            else:
                dp[i][j] = dp[i-1][j][:]
        else:
            dp[i][j] = dp[i-1][j][:]

        #print(dp[i][j])

if Len_Of_bag:
    print(*dp[Len_Of_bag-1][X][1])
else:
    print('0 0 0 0')
            
'''
1235 0 123 0 24

'''

# [[1, 1, 'A'], [2, 2, 'A'], [1, 1, 'A'], [1, 1, 'A'], [5, 1, 'B'], [10, 2, 'B'], [10, 1, 'C'], [25, 1, 'D'], [25, 1, 'D']]

