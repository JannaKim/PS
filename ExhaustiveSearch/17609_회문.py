for _ in range(int(input())):
    s= input()
    left=0
    right= len(s)-1
    passed=False
    while left<right:
        if s[left]==s[right]:
            left+=1
            right-=1
            continue
        if s[left+1]==s[right] and s[left]==s[right-1]:
            if passed:
                print(2)
                break
            tst= s[left+1:right+1][::-1]
            if tst==s[left+1:right+1]:
                print(1)
                break
            tst=s[left:right][::-1]
            if tst==s[left:right]:
                print(1)
                break
        elif s[left+1]==s[right] or s[left]==s[right-1]:
            if passed:
                print(2)
                break
            passed=True
            left+=1
            right-=1
        else:
            print(2)
            break
    if left>=right:
        if passed:
            print(1)
        else:
            print(0)
