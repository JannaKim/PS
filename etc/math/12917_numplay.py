p1, p2, p3, x1, x2, x3= map(int, input().split())

# prime
'''
for i in range(1, 300+1):
    for j in range(2, i):
        if not i%j:
            break
        if j==i-1:
            print(i)
'''


# x + p1*p2*p3
flag= False
for i in range(1, (p1*p2*p3)+1):
    if i%p1==x1 and i%p2==x2 and i%p3==x3:
        print(i)
        flag= True
        break
if not flag:
    print(-1)

#print(23300238%281, 23300238%283, 23300238%293)
