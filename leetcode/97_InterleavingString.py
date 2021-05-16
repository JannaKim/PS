class Solution:
    def __init__(self):
        self.n=0
        self.m=0
        self.l=0
        self.s1=''
        self.s2=''
        self.s3=''

    def topdown(self, left, right):
        if left==self.n-1 and right==self.m-1:
            return True
        if left>self.n or right>self.m:
            return False
        tst=False
        if left+right+2>=self.l:
            return False
        tst= tst or  (left+1<self.n and self.s3[left+right+2]==self.s1[left+1] and self.topdown(left+1, right))
        tst= tst or  (right+1<self.m and self.s3[left+right+2]==self.s2[right+1] and self.topdown(left, right+1))
        return tst

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.n= len(s1)
        self.m= len(s2)
        self.l=len(s3)
        if self.n+self.m!=self.l:
            return False
        return self.topdown(-1,-1)


sol1= Solution()
print(sol1.isInterleave("","","a"))



    