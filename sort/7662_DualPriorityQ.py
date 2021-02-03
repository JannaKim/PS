t= int(input())
for _ in range(t):
    class Heap():
        def __init__(self):
            self.q= []
            self.last_idx= -1
        
        def insert(self, data):
            self.q.append(data)
            self.last_idx+=1
            newcomer= self.last_idx
            while 0<=(newcomer-1)//2: # while parent node exists
                parent_idx = (newcomer-1)//2
                if self.q[parent_idx]< self.q[newcomer]:
                    self.q[parent_idx], self.q[newcomer]= self.q[newcomer], self.q[parent_idx]
                    newcomer= parent_idx
                else: break
            #print(self.q)
            
        
        def mx_del(self): # swap mx, mn and delete mx
            if self.last_idx<0:
                return -1
            self.q[0], self.q[self.last_idx]= self.q[self.last_idx], self.q[0]
            self.q.pop()
            self.last_idx-=1 #
            self.heapifydown(0)
        
        def mn_del(self):
            if self.last_idx<0:
                return -1
            until=(self.last_idx-1)//2 # smallest idx of parent node
            i=self.last_idx-1
            mn=self.q[self.last_idx]
            mn_idx=self.last_idx
            while until<i: # idx error.
                if mn> self.q[i]:
                    mn= self.q[i]
                    mn_idx=i
                i-=1
            # smallest one is in mn_idx
            self.q[mn_idx], self.q[self.last_idx]= self.q[self.last_idx], self.q[mn_idx]
            self.q.pop()
            if mn_idx!=self.last_idx:
                heapify_up= mn_idx
                while 0<=heapify_up: # heapify up
                    parent_idx = (heapify_up-1)//2
                    if 0<= parent_idx and self.q[parent_idx]< self.q[heapify_up]:
                        self.q[parent_idx], self.q[heapify_up]= self.q[heapify_up], self.q[parent_idx]
                        heapify_up= parent_idx
                    else: break
            self.last_idx-=1 #

        def heapifydown(self, idx):
            heapify_this= idx
            heapify_to_here=0
            while True:
                L= 2*heapify_this+1
                R= 2*heapify_this+2
                if L<=self.last_idx and self.q[L]>self.q[heapify_this]:
                    heapify_to_here= L
                    self.q[heapify_this], self.q[heapify_to_here]= self.q[heapify_to_here], self.q[heapify_this]
                    heapify_this= heapify_to_here
                elif R<=self.last_idx and self.q[R]>self.q[heapify_this]:
                    heapify_to_here= R
                    self.q[heapify_this], self.q[heapify_to_here]= self.q[heapify_to_here], self.q[heapify_this]
                    heapify_this= heapify_to_here
                else:
                    break

    hip= Heap()
    n= int(input())
    for _ in range(n):
        operate, num= input().split()
        if operate=='I':
            hip.insert(int(num))
        else:
            if num=='1':
                hip.mx_del()
            else:
                hip.mn_del()
    if hip.last_idx<0:
        print('EMPTY')
    else:
        #print(hip.q)
        print(hip.q[0], end=' ')
        until=(hip.last_idx-1)//2 # smallest idx of parent node
        i=hip.last_idx-1
        mn=hip.q[hip.last_idx]
        mn_idx=hip.last_idx
        while until<i:
            if mn> hip.q[i]:
                mn= hip.q[i]
                mn_idx=i
            i-=1
        print(hip.q[mn_idx])




            

