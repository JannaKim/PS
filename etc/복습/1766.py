from heapq import heappush as push, heappop as pop
#가능한 쉬운 문제부터 풀어야 하니 PriorityQ로 풀어야한다
N, M = map(int, input().split())
prob_info=[[] for _ in range(N+1)]
indegree=[-1]+[0]*(N)

for _ in range(M):
    A, B = map(int, input().split())
    prob_info[A].append(B)
    indegree[B]+=1

order=[]


stack=[]
poporder=[]
def heapq():
    q = []
    [push(q,book) for book in range(1,N+1) if indegree[book]==0]

    # indegree 0 짜리들로 dijik 시작
    global stack
    [stack.append(book) for book in range(1,N+1) if indegree[book]==0]
    print(f'{"시작":<10}{"= "}{stack}')
    global poporder
    while q:
        prob=pop(q)
        poporder.append(prob)
        order.append(prob)
        print(f'{"from= "}{prob}')
        for harder in prob_info[prob]:
            indegree[harder]-=1
            if indegree[harder]==0:
                print(f'{"to= ":>15}{harder}')
                push(q,harder)
                stack.append(harder)
        stack.remove(prob)
        print(f'{"stack":>30}{stack}')

heapq()
#print(prob_info)
print(f'{"stack":<10}{"= "}{stack}')
print(f'{"poporder":<10}{"= "}{poporder}')
print(*order)


'''
먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
가능하면 쉬운 문제부터 풀어야한다
4 2
4 2
3 1

5 3
3 2
5 1
1 2

12 15
5 6
5 2
5 12
6 2
6 3
6 10
10 11
10 1
2 1
1 9
1 7
9 4
11 8
3 8
3 4
'''
            


