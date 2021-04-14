# 1: 1h 10min
import sys; input= lambda: sys.stdin.readline().rstrip()
answer=[]
cnt=0
def solution(tickets):
    global cnt, answer
    dic={}
    edge={}
    incode={}
    decode={}

    cnt=0
    for a, b in tickets:
        if a+b not in dic:
            dic[a+b]=0
        dic[a+b]+=1
        if a not in incode:
            incode[a]=cnt
            decode[cnt]=a
            cnt+=1
        if b not in incode:
            incode[b]=cnt
            decode[cnt]=b
            cnt+=1
        if a not in edge:
            edge[a]=[]
        if b not in edge: ########################### 경로 없다면 딕 만들어지지도 않았음
            edge[b]=[]
        edge[a].append(b)

    #print([decode[a] for a in edge.keys()])  

    def dfs(v, num, road):
        v= decode[v]
        #print('num', num, [decode[el] for el in road])
        global cnt
        if not num:
            global answer
            if not answer: ###??????
                for el in road:
                    answer.append(decode[el])
                return True
            return False
        
        
        if not edge[v]:
            return False
        #print(v, edge[v])
        flag=False
        for v2 in sorted(edge[v]):
            #print(v, v2, dic[v+v2])
            if dic[v+v2]>0:
                flag=True
                dic[v+v2]-=1
                road.append(incode[v2])
                if dfs(incode[v2], num-1, road):
                    return True##???????
                road.pop()
                dic[v+v2]+=1
        if not flag:
            return False
    #print(cnt)
    ##### sort 한번만
    dfs(incode['ICN'], len(tickets),[incode['ICN']])
    return answer




#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]))

