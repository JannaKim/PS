# from 11:35 ~ 
# 12:43 WA 
# 13:21 AC
'''
많아야 한 사람

키같 춤 x

-1500 하고 시작
있는앤지 없는앤지?
있는애만 자기 인덱스 가리키고, 없는애는 있는 오른쪽 애 가리키도록

뒤에서 부터 돌아서 없는애면 앞에애랑 유니온

남자 기준으로 pair up
'''
def find(par, v):
    if par[v] == v or par[v] == -1:
        return par[v]
    else:
        par[v] = find(par, par[par[v]])
        return par[v]


def tallunion(par, u, v):
    r1 = find(par, u)
    r2 = find(par, v)

    par[r1] = r2

def shortunion(par, u, v):
    r1 = find(par, u)
    r2 = find(par, v)

    par[r1] = r2

tall_w = [0] * 1002
short_w = [1001] * 1002

tm, sm, tw, sw = {}, {}, {}, {}
n = int(input())

men = [*map(int, input().split())]

for el in men:
    if el > 0: # 키큼 선호
        el -= 1500
        if el not in tm:
            tm[el] = 0
        tm[el] += 1
    else:
        el = abs(el) - 1499
        if el not in sm:
            sm[el] = 0
        sm[el] += 1

women = [*map(int, input().split())]

for el in women:
    if el > 0: # 키큼 선호
        el -= 1499
        tall_w[el] = el
        if el not in tw:
            tw[el] = 0
        tw[el] += 1
    else:
        el = abs(el) - 1500
        short_w[el] = el
        if el not in sw:
            sw[el] = 0
        sw[el] += 1

#print(tall_w)
#print('\n')
for i in range(999, -1, -1): # 1000짜리 없으면 걘 0임
    if short_w[i] == 1001:
        short_w[i] = short_w[i + 1]
for i in range(1, 1002):
    if tall_w[i] == 0:
        tall_w[i] = tall_w[i - 1]



ans = 0
for k, v in tm.items():
    k += 1
    for _ in range(v):
        find(short_w, k)
        if short_w[k] != 1001: # exists
            #print(short_w[k])
            ans += 1
            if sw[short_w[k]] == 1:
                tallunion(short_w, short_w[k], short_w[k] + 1)
            else:
                sw[short_w[k]] -= 1  # ??
        


for k, v in sm.items():
    k -= 1
    #print(k, v)
    for _ in range(v):
        find(tall_w, k)
        if tall_w[k] != 0:
            ans += 1
            #print(k)
            #print(tall_w[k])
            if tw[tall_w[k]] == 1:
                shortunion(tall_w, tall_w[k], tall_w[k] - 1)
            else:
                tw[tall_w[k]] -= 1
        #print(tall_w, '\n', '\n')

#print(tall_w, short_w, sep='\n')
print(ans)


'''
3
-1600 -1600 -1600
1501 1501 1600
'''