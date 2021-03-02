a= input()
b= input()
def go(B):
    if len(a)==len(B):
        return a==B
    if B[-1]=='A' and go(B[:-1]):
        return True
    else:
        return B[0]=='B' and go(B[1:][::-1])
if go(b):
    print(1)
else:
    print(0)