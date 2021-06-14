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
1. dp: optimal substructure 
overlapping sub prob


2. bruteforce : O(n^2)
 - backtracking
3. binary : n : x

4. data strcuture
 - deque , pq , stc

5. graph
 - bfs , dfs

6. greedy

7. topology

8. shortest path
    = bellman, floyd, dijiksta

9. mst
    - prim ********
    - kruskal

10. divide  and conquer

11. two pointer

12. trie




'''
