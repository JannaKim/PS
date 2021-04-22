p1, p2, p3, x1, x2, x3= map(int, input().split())

# prime
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

p1, p2, p3, x1, x2, x3 = map(int,input().split())
for i in range(x1, p1*p2*p3, p1):
    if i%p2==x2 and i%p3==x3: print(i); break
else: print(-1)