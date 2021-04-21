def solution(gems):
    lt=0
    rt=0
    stc={}
    n=0 # 보석개수
    for idx,g in enumerate(gems):
        if g not in stc:
            stc[g]=0
            n+=1
    ans=1e9
    cn=1
    left=0
    right=0
    m=len(gems)
    stc[gems[0]]+=1
    while rt<m and lt<m:
        #print(lt,rt, cn)
        if cn<n:
            rt+=1
            if rt==m:
                break
            if stc[gems[rt]]:
                stc[gems[rt]]+=1
            else:
                stc[gems[rt]]+=1
                cn+=1
        else:
            if ans>rt-lt:
                left=lt
                right=rt
                ans=rt-lt
            lt+=1
            if lt==m:
                break
            #print(stc[gems[lt]], gems[lt])
            if stc[gems[lt-1]]>1:
                stc[gems[lt-1]]-=1
            else:
                cn-=1
                stc[gems[lt-1]]-=1
            
            



    return [left+1,right+1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
#solution(['a','b','c','a','b','b','c','b','a','d'])
#solution(["AA", "AB", "AC", "AA", "AC"])
#["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA","RUBY", "EMERALD"]
#print(solution(	["AA", "AB", "AC", "AA", "AC"]))