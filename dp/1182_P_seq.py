n, s= map(int, input().split())
L=[*map(int, input().split())]


dic={}
def knapsack(i, sm):
    if i>=n: return
    if sm+L[i] in dic:
        dic[sm+L[i]]+=1
    else:
        dic[sm+L[i]]=1

    knapsack(i+1, sm+L[i])
    knapsack(i+1, sm)

knapsack(0, 0)

if s in dic:
    print(dic[s])
else:
    print(0)

