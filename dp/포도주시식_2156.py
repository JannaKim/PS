N = int(input())
wine=[]
for i in range(N):
    wine.append(int(input()))
print(wine)
# 시작 = ox, oo, xo
def drink(i, a, b,sum): # a = 전꺼, b = 전전꺼
    if i==0:
        if a==1 and b==1:
            return sum
        else:
            return sum+wine[0]
    else:
        max=0
        if a==1 and b==1: #oo면
            return drink(i-1,0,1, sum)
        elif a==0 and b==0:
            return drink(i-1,1,0,sum+wine[i])
        else:
            return max(drink(i-1,0,a,sum), drink(i-1,1,a,sum+wine[i]))




print(max(drink(N-3, 1, 0, wine[N-2]), drink(N-3, 0, 1, wine[N-1]), drink(N-3, 1, 1, wine[N-2]+wine[N-1])))
