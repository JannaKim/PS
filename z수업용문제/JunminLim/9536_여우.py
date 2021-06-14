n=int(input())

for i in range (n):
    Ans=[]
    RAns=[]
    S=input().split()
    while "what does the fox say?" not in Ans:
        a=input()
        Ans.append(a)
        '''
        dog goes woof
fish goes blub
elephant goes toot
seal goes ow==ans
'''
    Ans.pop()
    for i in Ans:
        RAns.append(i.split())
    RRAns=[]
   
    for i in range (len(RAns)):
        RRAns.append(RAns[i][2])
    ans = []
    for a in S:
        if a in RRAns:
            continue
        ans.append(a)
    print(*ans)