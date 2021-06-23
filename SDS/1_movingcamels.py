dp = {}
L = []
n = -1
ans = 1e9

def backtrack(s, bitmask):
    global n, ans
    #print(s, bin(bitmask)[2:])

    for i in range(n):
        if (1 << i) & bitmask:
            flag = False
            for j in range(n):
                if i == j:
                    continue
                if (1 << j) & bitmask:
                    flag = True
                    bitmask -= (1 << i)
                    bitmask -= (1 << j)
                    s += max(L[i], L[j])
                    #print(s, bin(bitmask)[2:])
                    if not bitmask:
                        ans = min(ans, s)
                        return 
                    tmp = 1e9
                    ride = -1
                    for k in range(n):
                        if not (1 << k) & bitmask and L[k]<tmp:
                            tmp = L[k]
                            ride = k
                    bitmask += (1 << ride) # 타고올 가장 작은 낙타 더함
                    s += L[ride]
                    
                    if bitmask not in dp:
                        dp[bitmask]= True
                        backtrack(s, bitmask)

                    s -= max(L[i], L[j])
                    s -= L[ride]
                    bitmask -= (1 << ride)
                    bitmask += (1 << i)
                    bitmask += (1 << j)
            if not flag:
                s += L[i]
                ans = min(ans, s)



                
                
def main():
    global L, dp, moved, ans, n
    T = int(input())
    for t in range(1, T + 1):
        ans = 1e9
        n = int(input())
        L =[*map(int, input().split())]
        dp.clear()
        moved= []
        
        backtrack(0, 2 ** n - 1)
        print(f'#{t} {ans}')
    
    
main()