import sys; input = lambda: sys.stdin.readline().rstrip()
#5 2 3 1 4 
# 가장 긴 증가수열을 찾되 연속된 수를 가진 증가수열을 찾는다

#dp[i]: i번째를 끝으로 하는 가장 긴 1차이 증가수열
N = int(input())
L = [0]+ [int(i) for i in input().split()]
indegree=[1]*(N+1)
chk=[False]*(N+1)
for i in range(1,N+1):
    chk[L[i]]=True
    if chk[L[i]-1]==True:
        indegree[L[i]]=indegree[L[i]-1]+1
        #print(L[i], indegree[L[i]])
print(N-max(indegree))

'''
5
5 2 4 1 3
'''

