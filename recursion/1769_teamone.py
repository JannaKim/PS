def recursive(num):
    global cnt
    global ans
    n=int(num)
    if n<10:
        ans=n
        return
    ans = sum(map(int,num))
    cnt += 1
    recursive(str(ans))

num = str(input())
cnt = 0
ans = 0
recursive(num)
print(cnt)
if ans%3==0:
    print("YES")
else:
    print("NO")

