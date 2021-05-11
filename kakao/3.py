def solution(n, k, cmd):
    do=[]
    for el in cmd:
        if el[0]=='Z':
            tmp=[]
            while do[-1]!='C':
                tmp.append(do.pop())
            do.pop()
            while tmp:
                do.append(tmp.pop())
        else:
            do.append(el)
    #print(do)
    dic={}
    ths='s'
    rev={}
    for i in range(n):
        dic[ths]=i
        rev[i]=ths
        ths=i
    dic[n-1]='e'
    rev['e']=n-1
    
    cur=k
    #print(do)
    #print('cur',cur)
    for el in do:
        #print(el)
        if el=='C':
            dic[rev[cur]], rev[dic[cur]], cur= dic[cur], rev[cur], dic[cur]
            if cur=='e':
                cur=rev[cur]
        else:
            cnt= int(el.split()[1])
            if el[0]=='D':
                for _ in range(cnt):
                    cur= dic[cur]
            else:
                for _ in range(cnt):
                    #print(cur)
                    cur= rev[cur]
        print(cur)
                
    cur =dic['s']
    res=['X']*n
    answer=[]
    while cur!='e':
        answer.append(cur)
        cur=dic[cur]
    for el in answer:
        res[el]='O'
    print(dic[3], rev[7])
    return ''.join(res)

print(solution(8, 0, ["D 1","C","D 1","D 1","C","C","C","C","C","C","C"]))