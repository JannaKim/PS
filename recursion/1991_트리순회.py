n= int(input())
right= {}
left= {}
for _ in range(n):
    p, l, r= input().split()
    left[p]=l
    right[p]=r

def preorder(node):
    if node=='.': return""
    return node+preorder(left[node])+preorder(right[node])
    
print(preorder('A'))

def inorder(node):
    if node=='.': return""
    return inorder(left[node])+node+inorder(right[node])
    
print(inorder('A'))

def postorder(node):
    if node=='.': return""
    return postorder(left[node])+postorder(right[node])+node
    
print(postorder('A'))