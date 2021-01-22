n=int(input())
s=input()
r=s[::-1]
ans=['']*n
for i, (a, b) in enumerate(zip(s, r)):
    if a==b and a=='?':
        ans[i]=ans[n-i-1]='a'
    elif a=='?':
        ans[i]=b
    else:
        ans[i]=a

print(''.join(ans))

'''
n=int(input())
l=list(input())
for i in range(n):
    if l[i] == '?':
        if l[n-i-1] == '?':
            l[i] = 'a'
            l[n-i-1] = 'a'
        l[i] = l[n-i-1]
print(''.join(l))


'''