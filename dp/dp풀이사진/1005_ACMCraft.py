import sys
sys.setrecursionlimit(2000)
T = int(input())
for _ in range(T):
    N, K = [int(i) for i in input().split()]
    b = []
    [b.append([]) for _ in range(N+1)]
    T = [0]+[int(i) for i in input().split()]
    for _ in range(K):
        to, go = [int(i) for i in input().split()]
        b[go].append(to)
    goal = int(input())
    print('idx=',end=' ')
    [print(f'{i+1:<{len(b[i+1])+(len(str(T[i+1])) if len(str(T[i+1]))>0 else 1)}}',end=' ') for i in range(len(T)-1)]
    print()
    print(' T = ',end='')
    [print(f'{T[i+1]:<{len(b[i+1])+(len(str(T[i+1])) if len(str(T[i+1]))>0 else 1)}}',end=' ') for i in range(len(T)-1)]
    print()
    print(' b = ',*b[1:], sep='')
    dp=[-1]*(N+1)
    mx=0
    dic={}
    for i in range(1,N+1):
        dic[i]=False
    def f(idx, acm,dic):
        global mx
        #mx=max(sum(T[key] for key,values in dic.items() if values==True),mx)
        mx=max(mx,acm)
        print(f'idx={idx}, acm={acm}')
        '''
        if dp[idx]!=-1: # already built
            return
        else:
            dp[idx]=1
        '''   
        for i in b[idx]:
            if dic[i]==False:
                dic[i]=True
                f(i,acm+T[i],dic)
                dic[i]=False
    dic[goal]=True
    f(goal,T[goal],dic)
    print(f'mx={mx}')
    print()        


'''
2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7


1
6 6
100 1 0 10 100 0
1 3
2 3
3 4
3 5
4 6
5 6
6

'''

