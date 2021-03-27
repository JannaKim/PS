'''
3
aaaaaaaaaaaaaaaaaaa a a
b b bbbbbb
a b c a b c
b a b b

3
b b p a b c
b b p b b q
b b q b c a
b b p b b q
'''
# 어떤 단어도 앵무새가 말하는 모든 문장을 통틀어 2번 이상 등장하지 않는다.
import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
n= int(input())

q= [[]for _ in range(n)]
for i in range(n):
    for el in input().split():
        q[i].append([el,False])
L=input().split()
mx=len(L)

def backtrack(i):
    #print(i)
    if i==mx:
        print('Possible')
        exit()
    #flag=False
    for j in range(n):
        for k in range(len(q[j])):
            if not q[j][k][1] and q[j][k][0]==L[i]:
                #flag=True
                #print(k,'th',q[j][k][0],'of',q[j])
                q[j][k][1]=True
                backtrack(i+1)
                q[j][k][1]=False
            elif not q[j][k][1]:
                break
    #if not flag:
    #    print('fail! restart')
backtrack(0)
print('Impossible')