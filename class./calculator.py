class Calculator:
    def __init__(self, a, b):
        self.operator=a
        self.operand=b

    def add(self):
        return self.operator+self.operand

    def sub(self):
        return self.operator-self.operand

    def mul(self):
        return self.operator*self.operand

    def div(self):
        return self.operator/self.operand

class AdvancedCalculator(Calculator): # Calculator의 기능을 그대로 물려받았다.
    def pow(self):
        return self.operator**self.operand

class SafeCalculator(Calculator):
    def div(self):
        if self.operand==0: return 0
        else: return self.operator/self.operand
    
f = Calculator(4,0) #객체 f의 타입은 Calculator이다.
#f.setdata(4,2) # 덮어쓰기..
print(f.operator)
print(f.add())
print(f.sub())
print(f.mul())
h = SafeCalculator(4,0)

print(h.div())
print(h.add())

g = AdvancedCalculator(4,2)
print(g.pow())