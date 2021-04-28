import sys; input= lambda:sys.stdin.readline().rstrip()
n, d, k, c= map(int, input().split())
sushi= [int(input()) for _ in range(n)]

dish={}
for el in sushi:
    if el not in dish:
        dish[el]=0
for i in range(k):
    dish[sushi[i]]+=1
sushi+=sushi[:]
ans= len(set(sushi[:k]+[c]))
prv=ans
#print(ans)
#print(dish.items())
for i in range(1,n):
    dish[sushi[i-1]]-=1
    if sushi[i-1]!=c and not dish[sushi[i-1]]:
        prv-=1
    dish[sushi[i+k-1]]+=1
    if sushi[i+k-1]!=c and dish[sushi[i+k-1]]==1:
        prv+=1
    ans= max(ans, prv)
    #print(i,prv)
print(ans)