a , p = map(int, input().split())
dic = {}
dic[a]= True
cnt = 1
while True:
    tmp = 0
    for el in str(a):
        tmp += int(el)**p
    if tmp not in dic:
        cnt += 1
        dic[tmp] = True
    else:
        if dic[tmp]:
            cnt -= 1
            dic[tmp] = False
        else:
            break
    a = tmp

print(cnt)