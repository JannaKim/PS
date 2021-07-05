s = input()
chevron = False
ans = []
stc = []
for el in s:
    if chevron:
        ans.append(el)
        if el == '>':
            chevron = False
    else:
        if el == '<':
            chevron = True
            if stc:
                ans.append(''.join(stc)[::-1])
                stc = []
            ans.append(el)
        elif el == ' ':
            if stc:
                ans.append(''.join(stc)[::-1])
                stc = []
            ans.append(el)
        else:
            stc.append(el)
if stc:
    ans.append(''.join(stc)[::-1])           
print(''.join(ans))