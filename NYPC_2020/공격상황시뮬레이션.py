import fractions #TLE


N, A, B = [int(i) for i in input().split()]
X = [0]*N # 공격수의 수
Y = [0]*N # A, B 랑 X, Y 는 다 정수
for i in range(N):
    p, q = [int(j) for j in input().split()]
    X[i] = p
    Y[i] = q

va_num = 0
va_fw = 0
for j in range(N): # 0~ 공격수명수-1
    #LF1  = a(x-A)
    a = fractions.Fraction(Y[j],(X[j]-A)) # 변수a는 기울기 # 이게 나의
    b = fractions.Fraction(Y[j]/(X[j]-B))
    #print(a,b)
    for i in range(N):#0~ 공격수명수-1 5
        if i != j:
            #print(j,"번이랑",i,"번이랑",a*(X[i]-A),"", Y[i],"랑", b*(X[i]-B),"" ,Y[i])
            if a*(X[i]-A) < Y[i] or b*(X[i]-B) < Y[i]: # 내 y좌표가 더 크면작으며는 유효공격수다
                #print("     O")
                va_num += 1
            #print("공격수", j , "랑",i," 비교해보자, valid_nm",va_num)
           
                #print("     X")
    #print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
               
    if va_num == N-1:
        va_fw += 1
    va_num =0
       
               
print(va_fw)

#print(fractions.Fraction(1000000000, 1000000001))
