def perform_math_operation(num1,num2,operator):
    if(operator=="+"):
        return num1+num2
    elif(operator=="-"):
         return num1-num2
    elif(operator=="*"):
         return num1*num2
    elif(operator=="/"):
         if num2==0:
            print("Second number cannot be Zero !!!")
         else:
              return num1/num2
    else:
         print("Enter the valid operator: ")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
op = input("Enter the opertor: ")

result= perform_math_operation(num1=a,num2=b,operator=op)
print(f"The result of {a} {op} {b} is : {result}")