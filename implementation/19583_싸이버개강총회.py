import sys

def cal(A):
    A = [*map(int , A.split(':'))]
    A = A[0]*60 + A[1]
    return A

S , E , Q = map(cal, input().split())


IN = {}
for line in sys.stdin:
    time, name = line.split()
    time = cal(time)
    if time <= S and name not in IN:
        IN[name] = False
        

    elif E <= time <= Q:
        if name in IN:
            IN[name] = True

print(sum( [1 if el else 0 for el in IN.values()]))

# print(sum([]))