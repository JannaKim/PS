import time


strToInt = time.time() 
a='9'*1000000
b = int(a)
print("strToInt :", time.time() - strToInt)

intToStr = time.time() 
c=str(b)
print("intToStr :", time.time() - intToStr )
