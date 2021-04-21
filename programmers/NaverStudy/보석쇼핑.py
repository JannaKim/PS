def solution(gems):
    dic={}
    score=1e9
    tst={}
    st=0
    ans={}
    for idx,g in enumerate(gems):
        if g not in tst:
            tst[g]=True
            st=idx
    #print(st)
    
    for idx,g in enumerate(gems):
        
        print('dic',list(dic.items()))
        if g not in ans:
            ans[g]=0
        ans[g]=idx
        #print(idx,g)
        if g not in dic: # new one found
            dic[g]=idx
        else:
            if idx<=st:
                dic[g]=idx
            else:
                lt=1e9
                rt=0
                for k, v in ans.items():
                    lt=min(lt,v)
                rt=idx
                #print(list(dic.items()))
                tmp=rt-lt
                print('tmp',tmp)
                if tmp<score:
                    #print('?')
                    dic[g]=idx
                    score=tmp
                    for k, v in dic.items():
                        dic[k]=ans[k]
                #print('to',list(dic.items()))
        if idx==st:
            score= max(dic.values())-min(dic.values())
            print('fst score', score)


        
    lt=1e9
    rt=0
    print(list(dic.items()))
    for v in dic.values():
        lt=min(lt,v)
        rt=max(rt,v)

    return [lt+1,rt+1]

#solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
#solution(['a','b','c','a','b','b','c','b','a','d'])
#solution(["AA", "AB", "AC", "AA", "AC"])
#["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA","RUBY", "EMERALD"]
print(solution(["XYZ", "XYZ", "XYZ"]))