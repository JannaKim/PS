# WA
n, k= map(int, input().split())


def f(remain, s, As, Bs, pair):
    if pair and not remain:
        return
    #print(s)
    if pair==k:
        print('B'*remain+s)
        exit()
    f(remain-1,'A'+s, As+1, Bs, pair+Bs)
    f(remain-1,'B'+s, As, Bs+1, pair)
    f(remain-1,s+'B', As, Bs+1, pair+As)
    f(remain-1,s+'A', As, Bs+1, pair)


f(n-1,'B',0,1,0)

