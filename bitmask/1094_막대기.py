#import time
log= [64]

n= int(input())

while sum(log)>n:
    
    #time.sleep(1)
    log.append(log[0]>>1)
    log.append(log[0]>>1)
    log.pop(0)
    #time.sleep(1)
    log.sort()
    if sum(log[1:])>=n:
        log.pop(0)
    log.sort()
    #print(log)

print(len(log))
