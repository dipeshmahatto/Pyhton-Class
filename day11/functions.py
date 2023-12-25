# function arguments:
#     1. positional argument 
#     2. keyword argument
#     3. default argument
#     4. arbitary argument
#     5. keyword arbitary argument


def person(name,address,phone):
    print(f"Your name is {name}, address is {address}, phone :{phone} ")

person("Dipesh","kathmandu",9803643491) #positional argument
person(name="Dipesh",phone=9819800670,address="kathmandu") #keyword argument
# advantages of keyword argument:
    # Readable 
    # position doesnt matters
    # allows us to pass agrument in any order

