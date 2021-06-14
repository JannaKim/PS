from heapq import heappop , heappush
def gcd(a , b):
    if not a*b:
        return a + b
    if a>b:
        return gcd(a%b , b)
    else:
        return gcd(b%a, a)


cycle = 0

n , m = map(int, input().split())
time = [*map(int, input().split())]
lcm = time[0]
for i in range(1,m):
    tmp = gcd(time[i] , lcm)
    lcm = (time[i]//tmp) * lcm

q = []
for i in range(m):
    heappush(q , (0 , time[i] , i + 1))

cnt = 0
ans = -1
stc =[]
#print(lcm)
while True:
    accum , t , num = heappop(q)
    stc.append(num)
    #print(accum , t , num)
    cnt +=1
    if cnt == n:
        ans = num
        break

    if accum == lcm:
        cycle = cnt
        break
    heappush(q , (accum+t , t , num))

if ans < 0:
    print(stc[(n % cycle)-1])
else:
    print(ans)
