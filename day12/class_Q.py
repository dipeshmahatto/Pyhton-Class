class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def Add(self):
        print(self.a+self.b)
    
    def Sub(self):
        print(self.a-self.b)

    def Mul(self):
        print(self.a*self.b)

    def Div(self):
        print(self.a/self.b)


num1= int(input("Enter First number: "))
num2= int(input("Enter Second number: "))
calculator = Calculator(num1,num2);
calculator.Add()
calculator.Sub()
calculator.Mul()
calculator.Div()
