# def greet(**kwargs):
#     printO(type**kwargs)#dict

# greet(name="Dipesh",name2="Hari")



def print_info(name,**kwargs):
    print(f"Your name is: {name}")
    for i,value in kwargs.items():
        print(i,": ",value)


name = input("Enter your name: ")
address = input("Enter your address: ")
age = int(input("Enter your age: "))
mobile_no= input("Enter your mobile number: ")

print_info(name=name,address=address,age=age,mobile_no=mobile_no)