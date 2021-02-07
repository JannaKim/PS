t= int(input())

for _ in range(t):
    a= input()

    def chk(lo, hi):
        if lo+1>=hi:
            return True
        end= hi
        for i in range(lo, (lo+hi)//2):
            if a[i] == a[end]:
                return False
            end-=1
        if chk(lo, (lo+hi)//2-1) and chk((lo+hi)//2+1, hi):
            return True

    if chk(0, len(a)-1):
        print('YES')
    else:
        print('NO')

# 1000110


