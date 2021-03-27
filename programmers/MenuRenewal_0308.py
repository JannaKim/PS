mx=[2]*11
candi=[[] for _ in range(11)]
Lenvalids= 0
mxC=1e9
isCourse=[False]*11
def solution(orders, course):
    global isCourse
    global mxC
    mxC= max(course)
    ORDERS=[]
    for alph in orders:
        ls=[False]*26
        for ch in alph:
            ls[ord(ch)-65]=True
        ORDERS.append(ls)
    global Lenvalids
    global mx,candi
    exist=[0]*26
    for ls in ORDERS:
        for idx,el in enumerate(ls):
            if el:
                exist[idx]+=1
    valids=[]
    for i in range(26):
        if exist[i]>1:
            valids.append(i)
    Lenvalids= len(valids)
    for el in course:
        isCourse[el]=True
    #print(isCourse)
    def backtrack(i, cnt,changed,chosen):
        global mxC, isCourse
        #print(i,cnt,changed,chosen)
        global Lenvalids

        if changed and isCourse[cnt]:
            global mx,candi
            gather=0
            for ls in ORDERS:
                #print(ls)
                #print(human)
                flag=True
                #print(chosen)
                #print()
                for idx in chosen:
                    if not ls[idx]:
                        flag=False
                        break
                if flag:
                    gather+=1
            s=[]
            for idx in chosen:
                s.append(idx)
            if mx[cnt]<gather:
                mx[cnt]=gather
                candi[cnt]=[s]
            elif mx[cnt]==gather:
                candi[cnt].append(s)
        if i==Lenvalids:
            return
        
        if cnt+1>mxC:
            return
        chosen.append(valids[i])
        backtrack(i+1,cnt+1,True,chosen)
        chosen.pop()
        backtrack(i+1,cnt,False,chosen)
                
    backtrack(0,0,False,[])
    answer=[]
    for r in course:
        for ls in candi[r]:
            s=''
            for idx in ls:
                s+=chr(idx+65)

            answer.append(s)


    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))


'''
모든 알파벳별로 안고르고 존재하는 알파벳중에서고름
첫 시도:
course에 있는 숫자 r 별로 nCr 백트래킹함: 85

2:
두 개 이상 뜬 알파벳 중에서만 고름
백트래킹으로 고른 숫자가 course 에 있으면 개수비교: 70

3:
알파벳 숫자로 바꾸고 배달: 70

4:
사람 최대 20명, 각 사람이 시킨 요리 불배열로 체크함

'''