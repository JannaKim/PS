import sys
s= input()
t= input()
start= len(s)
end= len(t)
def rec(s, i):
    if i==end:
        if s==t:
            print(1)
            sys.exit()
        else:
            return
    a= s+'A'
    ra= a[::-1]
    le= i+1
    for j in range(end-le+1):
        if t[j:j+le]== a or t[j:j+le]==ra:
            found= True
            rec(a, i+1)
            break


    b= 'B'+s[::-1]
    rb= b[::-1]
    for j in range(end-le+1):
        if t[j:j+le]== b or t[j:j+le]==rb:
            found= True
            rec(b, i+1)
            break
rec(s, start)
print(0)
    
