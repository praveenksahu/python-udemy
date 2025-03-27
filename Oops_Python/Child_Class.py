from Oops_Python.Function_UnderClass import Calculator


class Child(Calculator):
    num2=150

    def __init__(self):
        Calculator.__init__(self,20,25)

    def addAllValues(self):
        return self.firstNum + self.secondName + self.summation()

obj = Child()
s=obj.addAllValues()
print(s)