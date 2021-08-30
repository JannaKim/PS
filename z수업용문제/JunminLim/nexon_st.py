m,f,n=map(int, input().split())
#n층 까지 가려면 계단을 n-1번 올라야 함
p=n//(m-1)
q=n%(m-1)
if q == f:
    print(p+1)
'''
if q < f:
   ''' 
