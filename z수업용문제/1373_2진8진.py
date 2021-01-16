import sys; input = lambda: sys.stdin.readline().rstrip(); r = range;enum= enumerate
bi=input()
oct=[]
length= len(bi)
mul3= length%3
if mul3:
    bi='0'*(3-mul3)+bi
    length+=(3-mul3)

for i in r(0,length,3):
    chunk=0
    for digit, j in enum(r(i,i+3)):
        #길이 n 문자로 이루어진 s에서 s.substr(3) 수행시간: O(n)
        if bi[j]=='1':
            chunk+= 2**(2-digit)
    oct.append(str(chunk))

print(''.join(oct))