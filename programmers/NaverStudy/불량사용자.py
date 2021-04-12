answer=set()
def solution(user, ban):
    user.sort()
    global answer
    
    
    n= len(user)
    m= len(ban)

    answer=0
    chk= [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            lu= len(user[i])
            lb= len(ban[j])
            if lu!=lb:
                continue
            flag=True
            for a, b in zip(user[i], ban[j]):
                if b=='*':
                    continue
                if a!=b:
                    flag=False
                    break
            if flag:
                chk[i][j]=1
    


    '''
    for i in range(m):
        if sum([el[i] for el in chk])==1: # 유일한 기로
            for j in range(n):
                if chk[j][i]==1:
                    chk[j]=[0]*m
                    chk[j][1]= 1
    '''
    '''
    for i in range(n):
        if sum(chk[i])==1:
            for j in range(m):
                if chk[i][j]==1: # 유일한 인풋
                    for k in range(n):
                        if k!=i:
                            chk[k][j]=0
    '''
    #print(user)
    #[print(*el) for el in chk]
    put= [False]*n

    answer=set()
    ans=[]
    def backtrack(i):
        #print(i, ans)
        if i==m:
            global answer
            answer.add(tuple(sorted(ans)))
            return


        for a in range(n):
            #print(i, j, a)
            #print(a,chk[a])
            if chk[a][i] and not put[a]:
                put[a]=True
                ans.append(user[a])
                backtrack(i+1)
                put[a]=False
                ans.pop()


    backtrack(0)



    return len(answer)

#print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))

#print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))

