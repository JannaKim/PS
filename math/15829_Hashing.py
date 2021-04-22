input()
a= input()
s=0
for idx, el in enumerate(a):
    s+=31**idx*(ord(el)-96)
    s%=1234567891
print(s)