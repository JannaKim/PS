def solution(new_id):
    ans=''
    for el in new_id:
        if ord(el)==ord('.'):
            ans+=el
        elif ord(el)==ord('_'):
            ans+=el
        elif ord(el)==ord('-'):
            ans+=el
        elif 97<=ord(el)<=ord('z'):
            ans+=el
        elif 65<=ord(el)<=ord('Z'):
            ans+=chr(ord(el)+(97-65))
        elif 48<=ord(el)<=57:
            ans+=el
            
    print(ans)
    new=''
    start=True
    for el in ans:
        if start and el=='.':
            new+='.'
            start=False
        elif not start and el!='.':
            new+=el
            start=True
        elif el!='.':
            new+=el
    if new[0]=='.':
        new=new[1:]
    if len(new)>1 and new[-1]=='.':
        new=new[:-1]
    if not new:
        new='a'
    ln=len(new)
    if ln>=16:
        new=new[:15]
    ln=len(new)
    if ln<=2:
        new+=new[-1]*(3-ln)
    if len(new)>1 and new[-1]=='.':
        new=new[:-1]
    print(new)
    return new
print(ord('0'),ord('9'),ord('.'))