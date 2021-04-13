import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())
inorder= [*map(int, input().split())]
postorder= [*map(int, input().split())]

class Tree:
    def __init__(self,v):
        self.left= None
        self.right= None
        self.parent= v

    def makeleft(self,v):
        self.left=v
    
    def makeright(self,v):
        self.right=v

trees= [0]*n
for i in range(n):
    flag=False
    trees[i]= Tree(i)
    for j in range(i-1, -1, -1):
        if inorder[j]==i: # 부모임
            flag=True
            trees[i].makeright(postorder[i-1])
            for k in range(i-1, -1, -1):
                if postorder[k]!=trees[i].right:
                    trees[i].makeleft(postorder[k])
                    break