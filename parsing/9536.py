for _ in range(int(input())):
    L=input().split()
    dic={}
    while True:
        line=input().split()
        if line[1]=='does':
            break
        dic[line[2]]=True
    for el in L:
        if el not in dic:
            print(el,end=' ')
