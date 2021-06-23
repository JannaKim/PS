'''
from itertools import combinations as combi
def solution(N, number):
    dp= {}
    for i in range(1,7):
        dp[int(str(N)*i)]=i
    dp[0]=0
    for _ in range(8):
        new={}
        L=list(dp.items())
        for el in combi(L,2):
            (k1, v1), (k2, v2)= el
            if v1+v2>8:
                continue
            #print(k1,v1,k2,v2)
            if k1+k2 in dp:
                new[k1+k2]=min(v1+v2, dp[k1+k2])
            else:
                new[k1+k2]=v1+v2
        for k, v in L:
            if k*N in dp:
                new[k*N]= min(v+1, dp[k*N])
            else:
                new[k*N]= v+1

            if k+N in dp:
                new[k+N]= min(v+1, dp[k+N])
            else:
                new[k+N]= v+1
            
            if k-N in dp:
                new[k-N]= min(v+1, dp[k-N])
            else:
                new[k-N]= v+1

            if not k%N:
                if k//N in dp:
                    new[k//N]= min(v+1, dp[k//N])
                else:
                    new[k//N]= v+1
        dp={}
        for k, v in new.items():
            dp[k]=v
    if number not in dp:
        return -1

    return dp[number]


print(solution(5,12),4)
'''

# dp[i] = j



'''
쓰는 숫자 개수로 나눔

숫자를 네개 썼을 때 만다는 숫자 셋

숫자 k개를 썼을 때 만들 수 있는 숫자 세트를

k개 숫자 만들 수 잇는


5

1 4 / 2 3 
한 스테이시 내에서 만들 수 있는 가짓수개 되게 많다

3 3 3 3

1 + 1 - 1
1 - 1 + 1 만드는 방법이 다르다

배열로 하면 한 step에 똑같은 숫자가 두번 들어간다는 것
set


'''