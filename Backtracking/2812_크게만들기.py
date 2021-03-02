n, k= map(int, input().split())

npt= input()
ans=[npt[0]]
cnt=0
connect=False
for idx,el in enumerate(npt[1:]):
    idx+=1
    flag= True
    if not connect:
        if int(ans[-1])<int(el):
            while ans and int(ans[-1])<int(el):
                flag=False
                ans.pop()
                cnt+=1
                if cnt==k:
                    connect= True
                    break
            ans.append(el)
            print(ans)
        if flag and int(ans[-1])>=int(el):
            if len(ans)==n-k:
                break
            ans.append(el)


    elif connect:
        if len(ans)==n-k:
            break
        ans.append(el)

    


print(''.join(ans))
'''

56561234
8 2


891

9781234

12345


2379


24351

4 1
8193

N, K = map(int, input().split())
number = input()
stack = []

last_pushed_idx = -1
for i in range(N):
    n = int(number[i])
    while len(stack) and stack[-1] < n and K > 0:
        stack.pop()
        K -= 1
    stack.append(n)

while K:
    stack.pop()
    K -= 1
print(''.join(map(lambda x: str(x), stack)))

'''