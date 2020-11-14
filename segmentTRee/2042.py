from math import *
N, M, K = map(int, input().split())
L = [] 
for _ in range(N):
    L.append(int(input()))

A = []
B = sum(L[1:]) #N
INFO = [[] for _ in range(N+1)] #N
#for i in range(1,N+1): #N


#node = [0]*2**(len(bin(N)[2:])+1) # 2^n~2^n+1
size = 2**(int(log(N,2))+2)+1
node = [0]*size



def tree(n,start, end):
    print(n,start, end)
    global node
    if start==end:
        node[n] = L[start]
        return node[n]
    node[n] = tree(2*n,start,(start+end)//2) + tree(2*n+1, (start+end)//2+1, end)
    return node[n]
tree(1,0,N-1) # 0번째 값은 0~n-1의 부모노드다
print(node)


for _ in range(M+K):
    a, b, c = map(int, input().split())
    '''
    if a==1:
        renew(b,c)
    if a==2:
        summ(b, c, 1, N)
    '''
'''   
def renew(a,b):

def summ(start, end, a, b):

'''


'''
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5 
'''