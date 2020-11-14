N = int(input())
cnslt=[]
for _ in range(N):
    cnslt.append([int(i) for i in input().split()])

dp=[0]*(N + 15)


print(f'ㅡㅡㅡㅡdp[i]= i일\'전\'까지 상담했을 때 받을 수 있는 최대 금액','\n')
print(dp)

for i in range(N):
    print(f'ㅡㅡㅡㅡㅡㅡㅡdp[{i+1} + {cnslt[i][0]}]: ({i+1}일전까지의 최선 스케쥴) + ({i+1}번째 상담) 조합,',end=' ')
    print(f'즉 {i+1 + cnslt[i][0]}일 전까지 완료되는 스케쥴중에 {i+1}번째 상담이 마지막 일정인 스케쥴이 최선이면 dp[{i+1} + {cnslt[i][0]}]가 바뀐다')
    if dp[i + cnslt[i][0]] < dp[i] + cnslt[i][1]:
        print(f'ㅡㅡㅡㅡㅡㅡㅡdp[{i + cnslt[i][0]+1}](={dp[i + cnslt[i][0]]}) <  dp[{i+1}](={dp[i]}) + {cnslt[i][1]}. 위 조합이 현재 상황까지 최선이므로 바꾼다')
        print(f'if 1) dp[{i + cnslt[i][0]+1}] = {dp[i + cnslt[i][0]]} -> ',end='')
        dp[i + cnslt[i][0]] = dp[i] + cnslt[i][1]
        print(dp[i + cnslt[i][0]])
    else:
        print(f'if 1) dp[{i + cnslt[i][0]+1}]: 변화 x.   dp[{i + cnslt[i][0]+1}](={dp[i + cnslt[i][0]]}) >= dp[{i+1}](={dp[i]}) + {cnslt[i][1]} 이므로 ')


    print(f'for문이 각 날짜를 한번씩 봐주는 걸 이용해, 스케쥴이 연결 안 돼있을 경우도 생각한 최상의 스케쥴을 전달해보자.')
    print(f'다음 날짜에만 전달해줘도 되는 이유: dp[다음날]은, 자기 날 전에 \'딱 맞춰\' 끝나는 애들중에서는 최선의 스케쥴을 받아온 상태다.')
    print(f'그런데 다음날 전에 딱 맞춰 끝나지 않는, 1일 이상 건너뛰는 다른 어떤 스케쥴이 돈을 더 많이 벌수 있는 경우가 있을 수 있다.')
    #dp[i + cnslt[i][0]] = max(dp[i + cnslt[i][0]], dp[i] + cnslt[i][1])

    if dp[i] > dp[i + 1]:
        print(f'    !!!   dp[{i+1}](={dp[i]}) > dp[{i + 1+1}](={dp[i+1]})')

        print(f'if 2) dp[{i + 1+1}] = {dp[i + 1]} -> ',end='')
        dp[i + 1] = dp[i]
        print(dp[i + 1])
    else:
        print(f'if 2) dp[{i+1+1}]: 변화 x.  dp[{i+1}](={dp[i]}) <= dp[{i+1+1}](={dp[i+1]})이므로')


    print(dp,'\n')

#print(dp[:N+1])
print(max(dp[:N + 1]))

'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''