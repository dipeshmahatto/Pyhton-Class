# def add(a,b) :
#     return a+b

# result = add(4,5)
# print(result)


# def SI(p,r,t):
#     return (p*t*r)/100

# p = int(input("Enter the principle amount: "))
# r = int(input("Enter the rate: "))
# t = int(input("Enter the time in months: "))
# SimpleInterst = SI(p,r,t)
# print(SimpleInterst)


def person(name, age:int):
    assert type(age)==int, "age must be interger"
    print("print name is ",name," and age  is ",age)

person("dipesh",20)