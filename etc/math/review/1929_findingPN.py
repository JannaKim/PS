m, n= map(int,input().split())
sieve= [True]*(n+1) # 모든수를 일단 소수가 맞다고 둔다
sieve[1]=False # 1은 소수가 아니다

for i in range(2,int((n)**(0.5))+1): # 파이썬 라이브러리 없이 루트 씌우는 법 + int로 감싸는 이유?
    # 왜 제곱근까지만 돌리면 될까? 어떤 수의 가능한 가장 큰 약수가 제곱근이기 때문.
    if sieve[i]: # 왜 소수로 남아있는 애들만 채치기 작업 하는지? 2로 채 쳤으면 4로 채 칠 필요없다.
        for j in range(2*i, n+1, i):
            sieve[j]=False # 소수가 아니므로 False로 변경
for k in range(m,n+1):
    if sieve[k]: # 이거랑 sieve[i]==True 같다.
        print(k)