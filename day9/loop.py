# a=1

# while a<5:
#     print(a)
#     a = a+1


# number = input("Enter a number: ")

# print(f"you have entered number {number}")



# Do while loop in python

# number = 10
# while True:
#     print(number)

#     if number>5:
#         break
# number= number+1

# while True:
#     number = input("Enter a number: ")

#     if (number.isdigit()):
#         print(f"You have entered {number}")
#         break
#     else:
#         print("Inavlid Input")

# Continue 
# numbers = [5,6,4,8,7,7]

# for number in numbers:
#     if number%2 != 0:
#         # continue
#         print(number)   

# Task management system 
# invoke user to input tassk 
# unvoke the user to input the task until user inputs 'exit' string 
# Once user exit the task input, print the task items 

tasks = []

while True:
    print("Enter 1 to close the program")
    user_input = input("Enter the task: ")

    if user_input == '1':
        break
    else:
        tasks.append(user_input)

print("Tasks entered:", tasks)
