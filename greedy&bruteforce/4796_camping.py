i=0
while(1):
    i+=1
    a, b, c= map(int, input().split())
    if a+b+c==0: break
    ans= c//b*a + (c%b if c%b<a else a)
    print(f'Case {i}: {ans}')