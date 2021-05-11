M=int(1e9)+7
s=0
dic={}

dic[1]=2
dic[0]=1
for i in range(2,31): # 1 2 4 8 16
    dic[i]= dic[i-1]*dic[i-1]%M
    #print(i, dic[i], dic[i-1])
    
'''
0 2
1 4
2 16
3 128
4 64
'''
for _ in range(int(input())):
    a, b= [*map(int, input().split())]
    if not b:
        continue
    bi= bin(b-1)[:1:-1]
    #print(bi)
    tmp=1
    for dig, el in enumerate(bi):
        #print(dig)
        #print(dig,int(el), dic[2**dig*int(el)])
        #print(dig*int(el))
        tmp*=dic[(dig+1)*int(el)]%M
        #print(tmp)
    s+=(a*b*tmp)%M
    #print(s)
print(s%M)

