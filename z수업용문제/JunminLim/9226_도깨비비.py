def swap(s, idx):
    a=s[:idx]
    b=s[idx:]
    t=b+a
    return t

def vowel(a):
    for i in range (len(a)):
        if a[i]== 'a' or a[i]== 'e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
            return i
    return 0


a=input()
while a!='#':
    p=swap(a,vowel(a))

    ans=p+'ay'
    print(ans)
    a=input()


