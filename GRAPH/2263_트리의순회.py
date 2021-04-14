import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
n= int(input())
inorder= [*map(int, input().split())]
postorder= [*map(int, input().split())]

ans=[]
def rec(lo, hi, k):
    #print(lo, hi, k)

    if inorder[lo]==k:
        
        if k!=inorder[hi]:
            if postorder:
                ths=postorder.pop()
                rec(lo+1,hi,ths)
        ans.append(inorder[lo])
        return
    
    for i in range(lo,hi+1):
        if inorder[i]==k:
            if i+1<=hi and postorder:
                rec(i+1,hi,postorder.pop())
            if postorder:
                rec(lo,i-1,postorder.pop())
            ans.append(inorder[i])

rec(0,n-1,postorder.pop())
print(*ans[::-1])

'''
class Tree:
    def __init__(self,v):
        self.left= None
        self.right= None
        self.parent= v
        self.me= v

    def makeleft(self,v):
        self.left=v
        trees[self.left].parent=self.parent
    
    def makeright(self,v):
        self.right=v
        trees[self.right].parent=self.parent

    def printnode(self):
        
        print(self.me)
        #print(self.left, self.right)
        if self.left!=None:
            trees[self.left].printnode()
        if self.right!=None:
            trees[self.right].printnode()
        

trees= [0]*(n+1)
for i in range(n):
    flag=False
    trees[postorder[i]]= Tree(postorder[i])
    for j in range(i, -1, -1):
        if inorder[j]==postorder[i] and i-1>=0: # 부모임
            flag=True
            #print(f'{postorder[i]}는 {postorder[i-1]}의 부모')
            trees[postorder[i]].makeright(postorder[i-1])
            for k in range(i-1, -1, -1):
                if trees[postorder[k]]==0:
                    continue
                #print('left?',postorder[k],trees[postorder[i-1]].parent)
                if trees[postorder[k]].parent!=trees[postorder[i-1]].parent:
                    #print(f'{postorder[i]}s left: {postorder[k]}')
                    trees[i].makeleft(postorder[k])
                    break
            trees[trees[postorder[i]].left].parent=postorder[i]
            trees[trees[postorder[i]].right].parent=postorder[i]
      
#print(inorder[0])
trees[postorder[-1]].printnode()
'''
'''
12
9 4 2 10 5 11 1 12 6 3 13 7
9 4 10 11 5 2 12 6 13 7 3 1

14
8 4 9 2 10 5 11 1 12 6 13 3 14 7
8 9 4 10 11 5 2 12 13 6 14 7 3 1

9
9 4 2 1 12 6 3 13 7
9 4 10 11 5 2 12 6 13 7 3 1
'''
