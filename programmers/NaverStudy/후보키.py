from itertools import combinations as combi
def solution(relation):
    m=len(relation[0])
    n= len(relation)
    chk= [[-1]*m for _ in range(n)]
    dic={}
    cnt=1
    for i in range(n):
        for j in range(m):
            if relation[i][j] not in dic:
                dic[relation[i][j]]=0 # 유일하면 0
            else:
                dic[relation[i][j]]=cnt
                cnt+=1

    for i in range(n):
        for j in range(m):
            chk[i][j]= dic[relation[i][j]]

    remain=[]
    for i in range(m):
        remain.append([dic[el[i]] for el in relation]+[i])

    print(remain)
    com={}
    for i in range(1,9):
        if len(remain)<i:
            break
        L= list(combi(remain,i))
        
        
        #print('L', L)
        for a in L:
            pair={}
            #print('a', a)
            flag=True
            for idx, b in enumerate(zip(*a)):
                if idx==n:
                    break

                sm=1
                tmp=[]
                for idx, el in enumerate(b):
                    print(el)
                    sm*=el
                    tmp.append(el)
                #tmp.sort()
                tmp=tuple(tmp)
                #print(tmp)
                if sm!=0:
                    #print(tmp,'?')
                    if tmp in pair:
                        #print('tmp in pair')
                        flag=False
                    else:
                        #print('new',tmp)
                        pair[tmp]=True
            if flag: # a 조합 통과
                candi= [el[-1] for el in a]
                #print('found', candi)
                f= True
                for t in range(1, len(candi)+1):
                    for ls in combi(candi,t):
                        if tuple(sorted(list(ls))) in com:
                            f=False
                            break
                if f:
                    #print('o')
                    #print(tuple(sorted(candi)))
                    com[tuple(sorted(candi))]=True



                    

    return len(com.keys())

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))