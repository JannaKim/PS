from collections import deque
from functools import binary
n = int(input())
L = [int(input()) for _ in range(n)]


recent = deque()
for i in range(n-1 , -1 ,-1):
    cur = L[i]

    bs(recent , cur)

# [1,2]
# [1,1,2,3,4,5,1,2,3,0,2]
'''
stack : LIFO
스택 유지 규칙
- 스택의 사이즈

규칙: 나보다 작은 ㄱ

import sys
input = sys.stdin.readline
n = int(input())
number = [input() for _ in range(n)]

answer = 0
stack = []
for height in number :
	while stack and stack[-1] <= height:
		stack.pop()
	answer += len(stack)
	stack.append(height)
print(answer)



'''
'''
1. dp: optimal substructure 
overlapping sub prob


2. bruteforce : O(n^2)
 - backtracking
3. binary : n : x

4. data strcuture
 - deque , pq , stc

11. two pointer

12. simul & imple

5. graph
 - bfs , dfs

6. greedy

7. divide  and conquer

8. shortest path
    = bellman, floyd, dijiksta

9. mst
    - prim ********
    - kruskal

10. topology 



13. trie

14. tree dp

15. 

15. seg tree

15. scc

16. string



'''
