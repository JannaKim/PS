n , k = input().split()
k = int(k)
m = len(n)
mx = int(n)
if m ==1:
    print(-1)
    exit()
ans = 0
semians = 0
remain = 1e9
dp = {}
def backtrack(num , cnt):
    #print(num , cnt)
    global ans , semians
    if not cnt:
        ans = max(ans , int(''.join(num)))
        return
    flag = False
    for i in range(m):
        for j in range(i + 1 , m):
            new = num[:]
            flag = True
            new[i] , new[j] = new[j] , new[i]
            if new[0]== '0':
                continue
            tmp = ''.join(new)+'_'+str(cnt) 
            if tmp not in dp:
                dp[tmp] = True
                flag = True
                backtrack(new , cnt - 1)
                
    if not flag:
        global remain
        tmp = int(''.join(num))
        if cnt < remain and tmp < semians:
            remain =  cnt
            semians = num[:]

        

backtrack(list(n) , k)
if ans:
    print(ans)
else:
    #print(semians , remain)
    if remain == 1e9:
        print(-1)
    elif remain % 2:
        semians[-1] , semians[-2] = semians[-2] , semians[-1]
        print(int(''.join(semians)))
    else:
        print(int(''.join(semians)))

'''
3970 3
9703
'''