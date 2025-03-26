#Class, Function

class Calculator():
    num=100

    def __init__(self,a,b):
        self.firstNum=a
        self.secondName=b

    def summation(self):
        return self.firstNum + self.secondName + Calculator .num

obj=Calculator(12,13)
s=obj.summation()

print(s)
