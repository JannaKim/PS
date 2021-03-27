from itertools import combinations


def solution(orders, course):
    stock=[0]*26
    valids=[]
    human=[]
    for customer in orders:
        tmp=[False]*26
        for onemenu in customer:
            stock[ord(onemenu)-65]+=1
            tmp[ord(onemenu)-65]=True
        human.append(tmp)
    for i in range(26):
        if stock[i]>1:
            valids.append(i)

    N= len(orders)
    
    mx= [2]*11
    ans= [[] for _ in range(11)]
    checked={}
    for person in orders:
        for el in course:
            person=sorted(list(person))
            mxSize= len(person)
            if el<=mxSize:
                for ls in combinations(person,el):
                    if ls in checked:
                        continue
                    else:
                        checked[ls]=True
                    gather=0
                    for i in range(N):
                        flag=True
                        for menuNum in ls:
                            if not human[i][ord(menuNum)-65]:
                                flag=False
                                break
                        if flag:
                            gather+=1
                    if mx[el]<gather:
                        mx[el]=gather
                        ans[el]=[ls]
                    elif mx[el]==gather:
                        ans[el].append(ls)
    answer=[]
    for Num in course:
        for ls in ans[Num]:

            s=''
            for alp in ls:
                s+=alp
            answer.append(s)

    return sorted(answer)
            


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))

'''
사람별로 만들 수 있는 조합뽑아서 전체랑 비교하는 게 더 빠르다? 왜?
어느 고객의 메뉴목록에도  존재하지 않는 n조합을 만들어서 비교해주는 게 손해기때문
'''