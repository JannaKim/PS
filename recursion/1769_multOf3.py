input= input()

cnt=0
def add(s):
    global cnt
    num= int(s)
    if num<10:
        print(cnt)
        if not num%3:
            print('YES')
        else:
            print('NO')
    else:
        cnt+=1
        sum=0
        for el in s:
            sum+=int(el)
        add(str(sum))

add(input)
    
