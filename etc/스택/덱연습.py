from collections import deque
D = deque()
[D.append(i) for i in range(1,10)]
print(D)

print(D.popleft())
print(D.pop())