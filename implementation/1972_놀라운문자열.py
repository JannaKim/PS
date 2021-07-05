
def check(s, n):
    
    for i in range(1, n):
        dic = {}
        for j in range(0, n):
            if j + i >=n:
                break
            #print(s[j], s[j + i])
            if s[j]+s[j + i] not in dic:
                dic[s[j]+s[j + i] ] = True
            else:
                return False
        #print('re')
    return True

while True:
    s = input()
    if s == '*':
        break
    n = len(s)
    
    if check(s, n):
        print(f'{s} is surprising.')
    else:
        print(f'{s} is NOT surprising.')

    

