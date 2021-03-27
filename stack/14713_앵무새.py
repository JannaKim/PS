import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())

q= [{} for _ in range(n)]
cnt=0
for i in range(n):
    for el in input().split():
        cnt+=1
        q[i][el]=cnt

saids={}
for el in input().split():
    found=False

    for thsparrot in q: # 앵무새별로 검사
        possible=False
        if el in thsparrot:
            #print(el, 'fnd in ths parrot')
            #print(thsparrot[el])
            standard= thsparrot[el]
            flag=True
            deleted=[]
            for k, v in thsparrot.items(): # 이전껄 다 말했는지?
                #if v<standard:
                #    print(k,f'{v}<{standard}','이거말했어야함')
                if v<standard and k not in saids:
                    flag=False
                    break
                elif v<standard and k in saids:
                    
            if flag: # 말다 말했어: 통과
                #print('다말햇어')
                possible=True
                break
            # 아니면 newparrot
    if possible:
        found=True
    saids[el]=True
    if not found:
        print('Impossible')
        exit()

print('Possible')

'''
3
aaaaaaaaaaaaaaaaaaa a a
b b bbbbbb
a b c a b c
b a b b

3
b b p a b c
b b p b b q
b b q b c a
b b p b b q
'''