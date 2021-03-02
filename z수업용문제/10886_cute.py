n =int(input())
vote= [0]*2
for _ in range(n):
    a= int(input())
    vote[a]+=1
if vote[0]>vote[1]:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')