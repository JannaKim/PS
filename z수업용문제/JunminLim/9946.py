cnt = 0
while True:
    cnt += 1
    a = input()
    b = input()
    if a == 'END' and b == 'END':
        break

    A=list(a)
    B=list(b)
    A.sort()
    B.sort()
    if A==B:
        print(f'Case {cnt}: same')
    else:
        print(f'Case {cnt}: different')
        
'''
testing
intestg
'''