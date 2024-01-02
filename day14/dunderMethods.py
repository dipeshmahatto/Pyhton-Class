class Bike:
    def __init__(self,name,cc):
        self.name= name
        self.cc = cc 

    def print_detail(self):
        print(f"Bike name {self.name} and cc is {self.cc}")

        # magic method --> This method called itself do no need to be called......

    def __str__(self) -> str:
        return f"{self.name} {self.cc}"
    
    def __gt__(self,other):
        return self.cc>other.cc
    
    def __add__(self,other):
        return self.cc + other.cc
    
bike= Bike("Raider",150)
bike2 = Bike("TVS" ,200)

print(bike<bike2)
print(bike+bike2)

