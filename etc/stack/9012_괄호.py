T = int(input())
for _ in range(T):
    s = list(input())
    if s[0]==')':
        print('NO')
        continue
    else:
        q=1
        del s[0]
        while len(s)>0:
            if s[0]==')':
                q-=1
            else:
                q+=1
            del s[0]
            if q<0:
                break
    if not q: print('YES')
    else: print ("NO")
