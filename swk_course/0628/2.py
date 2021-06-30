from collections import deque
'''
if waitlist, bridge empty: end
if sum(onbringe) + waitlist[-1] > wei:
    onbridge.append(0)
    onbridge.popleft()

'''
n, bridgelen, wei = map(int, input().split())
waitlist = [*map(int,  input().split())][::-1] # 반대로 받아서 pop
onbridge = deque()
for _ in range(bridgelen):
    onbridge.append(0)
time = 0
while waitlist or onbridge:
    onbridge.popleft()
    if waitlist:
        if sum(onbridge) + waitlist[-1] > wei:
            onbridge.append(0)
        else:
            onbridge.append( waitlist.pop() )  
    else:
        time += bridgelen
        break
    
    time += 1
    #print(onbridge)
print(time)
