#1769 3의 배수
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
        return
    cnt+=1
    sumup=sum([int(el) for el in s])
    add(str(sumup))

add(input)
    
