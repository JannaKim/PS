# 5,6 번은 시간없어서 짜다 말았었어요
'''
2
1 3 1 3 5
2 2 2 4
3 2 1 2
4 1 3

13
'''
n=int(input())

dic={}
mole=[0]*(n**2+1)
for i in range(1,n**2+1):
    a, num,*b, =[*map(int, input().split())]
    mole[a]=b

ans=0 
# 시간복잡도?
for i in range(n**2,0,-1): # 25
    for t in mole[i]: # 100
        if t not in dic: # 1 ?
            dic[t]=1
            ans+=i
print(ans)

'''
두더지 최대 25마리
두더지별 올라오는 횟수 최대 100
'''


