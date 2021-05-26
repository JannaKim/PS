from itertools import combinations as combi
def solution(relation):
    r= len(relation)
    c= len(relation[0])
    dic={}
    table= [[-1]*c for _ in range(r)]
    idx=0
    for i in range(r):
        for j in range(c):
            if relation[i][j] not in dic:
                dic[relation[i][j]]=idx
                table[i][j]=idx
                idx+=1
            else:
                table[i][j]=dic[relation[i][j]]
    for i in range(r):
        for j in range(c):
            table[i][j]= str(table[i][j])
                
    [print(*el) for el in table]
    answer = 0
    done= [0]*c
    for i in range(1,c+1):
        for ls in combi(list(range(c)),i):
            print(ls)
            s=0
            s=sum([done[el] for el in ls])
            if s:
                continue
            chk={}
            flag=False
            for j in range(r):
                chunk=''
                for idx in ls:
                    chunk+=table[j][idx]+' '
                print(chunk)
                if chunk not in chk:
                    chk[chunk]=True
                else:
                    flag=True
                    break
            if not flag:
                for idx in ls:
                    done[idx]=1
                answer+=1
            print('done',done)

    return answer


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))