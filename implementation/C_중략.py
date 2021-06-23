n = int(input())
s = input()
if n <= 25:
    print(s)
else:
    mid = s[11:-11]
    m = len(mid)
    es = mid.replace('.','')

    if mid[-1] == '.' and len(es) == m-1:
        print(s[:11]+'...'+s[-11:])
    elif len(es) == m:
        print(s[:11]+'...'+s[-11:])
    else:
        print(s[:9]+'......'+s[-10:])

#AAAAAAAAAA.CCCC.BBBBBBBBBB.