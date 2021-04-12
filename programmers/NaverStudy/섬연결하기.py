# 1: 6h
def solution(n, costs):
    ans = 0
    costs.sort(key = lambda x: x[2]) 
    r = set([costs[0][0]]) 
    while len(r)!=n:
        for i, cost in enumerate(costs):
            if cost[0] in r and cost[1] in r:
                continue
            if cost[0] in r or cost[1] in r:
                r.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans


#print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
#print(solution(5, [[0,1,1],[0,2,1],[0,3,1],[0,4,1],[1,2,100],[2,3,100],[3,4,100]]))
#print(solution(4, [[0,1,1],[0,2,1],[1,2,5],[1,3,1],[2,3,1]]))
print(solution(5, [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]])

'''
MST
'''