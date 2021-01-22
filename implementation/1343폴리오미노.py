import sys
s=input()
L=s.split('.')
end=len(L)-1
ans=[]
for idx,el in enumerate(s.split('.')):
    cur= len(el)
    if cur%2:
        print(-1)
        sys.exit()
    ans.append('AAAA'*(cur//4))
    ans.append('B'*(cur%4))
    if idx!=end:
        ans.append('.')
print(''.join(ans))
