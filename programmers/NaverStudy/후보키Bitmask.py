def solution(relation):
    n= len(relation)
    m= len(relation[0])

    ans=[]
    Len=m
    for i in range(1,2**m):
        
        ths= bin(i)[2:]
        combi= '0'*(Len-len(ths))+ths
        ls={}
        flag=True
        for j in range(n): # 인원별로 돌림
            line=[]
            for idx, b in enumerate(combi):
                if b=='1':
                    line.append(relation[j][idx])
            if tuple(line) in ls:
                flag=False
                break
            else:
                ls[tuple(line)]=True
        if flag:
            possi=True
            for b in ans:
                int(combi,2)
                if b&int(combi,2)==b:
                    possi=False
                    break
            if possi:
                ans.append(int(combi,2))
    
    return len(ans)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))