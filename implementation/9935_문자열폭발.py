s= input()
ths=input()
n= len(s)
m=len(ths)
#1 2 3 4 5
cur=0

flag=True
while flag:
    remain=[True]*n
    flag=False
    for i in range(n):
        if s[i]==ths[cur]:
            cur+=1
            if cur==m:
                flag=True
                for j in range(i,i-m,-1):
                    remain[j]=False
                cur=0
        else:
            cur=0
            if s[i]==ths[cur]:
                cur+=1
    s=''.join([(s[i] if remain[i] else '') for i in range(n)])
    n=len(s)
print([s,'FRULA'][not s])
# 10: z

'''
aabcbcabcaa
bca
'''