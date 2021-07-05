H = [False] * 26
n = int(input())
L = [input() for _ in range(n)]

def chunk(s):
    res = ''
    found = False
    for el in s.split():
        alp = ord(el[0].lower()) - 97 
        if found:
            res += el+ ' '
        
        elif not H[alp]:
            found = True
            H[alp] = True
            res += '[' + el[0] + ']' + el[1:] + ' '
        else:
            res += el + ' '

    if found:
        if len(res) <= 1:
            print(res)
        else:
            print(res[:-1])
        return True
    return False
        

def line(s):
    res = ''
    found = False
    for el in s:
        if el == ' ':
            res+=el
            continue
        alp = ord(el.lower()) - 97 
        if found:
            res += el
        elif not H[alp]:
            H[alp] = True
            found = True
            res += '[' + el+ ']' 
        else:
            res += el
    if found:
        print(res)
        return True
    return False

        
    
for i in range(n):
    tmp = L[i]
    if not tmp.replace(' ', ''):
        print(L[i])
    elif not chunk(L[i]):
        if not line(L[i]):
            print(L[i])