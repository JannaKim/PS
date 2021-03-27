t= int(input())

for _ in range(t):
    n= int(input())

    dic={}
    for _ in range(n):
        a, b= input().split()
        if b in dic:
            dic[b]+=1
        else:
            dic[b]=1

    print('keys')
    for k in dic.keys():
        print(k)
    print('values')  
    for v in dic.values():
        print(v)
    print('items')
    for k, v in dic.items():
        print(k,v)