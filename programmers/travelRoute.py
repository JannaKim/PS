import sys; sys.setrecursionlimit(1000000)
unused=0 # num of tickets
def solution(tickets):
    tmp= set() # set of airports
    global unused
    for a, b in tickets:
        tmp.add(a)
        tmp.add(b)
        unused+=1

    enum = list(tmp)
    enum.sort() # sort airports

    # match airports with 0~n-1, alphabetically
    decode={} # num -> airports
    code={} # airports -> num

    for i, el in enumerate(enum):
        decode[i]= el
        code[el]=i

    ports= len(tmp) 


    edge= [[] for _ in range(ports+1)]
    #remain={}
    remain= [[0]*ports for _ in range(ports)]

    for a, b in tickets:
        #if (code[a],code[b]) in remain:
        #    remain[(code[a],code[b])]+=1
        #else:
        #    remain[(code[a],code[b])]=1
        edge[code[a]].append(code[b]) 
        remain[code[a]][code[b]]+=1 # raise current ticket's amount
    
    #for k, v in remain.items():
    #    print(decode[k[0]], decode[k[1]], v, end='  ')
   
    for v in range(ports):
        edge[v].sort() # sort each edge
    
    ans=[]
    def dfs(v):
        global unused
        #print(decode[v])
        #[print(*el) for el in used]
        ans.append(decode[v])
        #print(ans, unused)
        
        if unused==0: # all tickets used: answer found
            return True

        ansFound=False
        mx=len(edge[v])**2
        for v2 in edge[v]:
            if remain[v][v2]>0: # unused ticket found
                remain[v][v2]-=1
                unused-=1
                if dfs(v2): #try
                    ansFound=True
                    break
                remain[v][v2]+=1 # wrong way: backtrack
                unused+=1
                if mx>0:
                    edge[v].append(v2) # append current ticket at the very back
                    mx-=1

        if ansFound: return True
        ans.pop()
        return False



    dfs(code['ICN'])
    if unused!=0:
        for i in range(ports):
            for j in range(ports):
                    for _ in range(remain[i][j]):
                        ans.append(decode[j])


    return ans

#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	))

#print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

#print(solution([["ICN", "ATL"], ["ICN", "ABC"], ["ATL", "SFO"], ["SFO", "ICN"]]))

#print(solution([["INC", "A"],["INC", "A"],["INC", "A"],["A", "INC"],["A", "INC"]] ))

#print(solution([['ICN', 'B'], ['B', 'C'], ['C', 'ICN'], ['ICN', 'D'], ['ICN', 'E'], ['E', 'F']]))

#print(solution( [["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))

print(solution([["ICN","A"],["A","B"],["B","A"],["A","ICN"],["ICN","A"]] ))

#print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
#[ICN, ATL, ICN, SFO, ATL, SFO]