import sys
def cantor(k):
    if k==1:
        return '-'
    a= cantor(k//3)
    return a+' '*(k//3)+a

for line in sys.stdin:
    n= int(line)
    print(cantor(3**n))