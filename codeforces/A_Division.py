T = int(input())
for _ in range(T):
    p, q = map(int,input().split())

    # x는 p의 약수, 
    i = 2
    L = [1,p]
    while i*i<p:
        if p%i==0:
            L.append(i)
            L.append(p//i)
        i+=1
        if i*i==p:
            L.append(i)
    L.sort()


    for i in L[::-1]:
        if i%q:
            print(i)
            break

'''
3  
10 4
12 6
179 822
'''

