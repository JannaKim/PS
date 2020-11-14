T = int(input())
for _ in range(T):
    L=[]
    for _ in range(int(input())):
        name, liq = [i for i in input().split()]
        L.append((name,int(liq)))
    L.sort(key = lambda x:x[1], reverse=True)
    print(L[0][0])
    

'''
2
3
Yonsei 10
Korea 10000000
Ewha 20
2
Yonsei 1
Korea 10000000
'''