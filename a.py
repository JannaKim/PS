import random

it = 9
N = it * 1000 + 1
print(N)


def tree(n): # 호출될 때마다 n~ n+999 1000개 만든다
    cnt = 1
    add = []
    print(1, 1, n) # 1
    add.append(n+1)
    for i in range(3, 1000, 2):
        rnd = []
        '''
        rnd = list(range(1,i+n-2+1))
        random.shuffle(rnd)
        '''
        for j in range(100):
            rnd.append(random.randint(1, i + n - 2))
        
        rnd = list(set(rnd))
        print(cnt, len(rnd), n, *rnd[1:]) # 499
        print(cnt, len(rnd), i+n-1, *rnd[1:]) # 499
        add.append(i+n)
        cnt += 1
    print(1, len(add), *add) # 1, len(add)=500

print(1, 0)
for i in range(it):
    tree(1 + i*1000)