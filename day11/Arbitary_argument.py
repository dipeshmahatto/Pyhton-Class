#Arbitary Arguments
def square(*args):
    for i in args:
        print(f"Square of {i} is: {i*i}")

square(5,4,2,12)