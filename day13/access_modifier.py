class Bike:
    def __init__(self,name,cc):
        self.name= name
        self.cc = cc 

    def print_detail(self):
        print(f"Bike name {self.name} and cc is {self.cc}")

bike = Bike("Raider",150)
bike.print_detail()



# public is default modifier
# protected (_variablename) this provides access only but cant change its value 
# private (__variablename) this provides no access and cannt change its value
