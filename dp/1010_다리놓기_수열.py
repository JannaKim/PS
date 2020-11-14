T = int(input())
# mCn= m! //( n! (= a) * (m-n)! (=b) )
for _ in range(T):
    N, M = map(int,input().split())
    C=b=a=1
    for i in range(2,M+1):
        C*=i
        if i==N:
            a=C
        if i==(M-N): # N == M=n 일 수 있으므로 elif 가 아닌 if 써야했다
            b=C
    print(C//(a*b)) 

