class Employee:
    def __init__(self,name,address, salary)->None:
        self.name=name
        self.address=address
        self.salary=salary
    def print_detail(self):
        print(f"Name : {self.name}")
        print(f"ADDRESS : {self.address}")
        print(f"salary : {self.salary}")
