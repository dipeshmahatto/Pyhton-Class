class Employee:
    def __init__(self,name,address, salary)->None:
        self.name=name
        self.address=address
        self.salary=salary

    def print_detail(self):
        print(f"Name : {self.name}")
        print(f"ADDRESS : {self.address}")
        print(f"salary : {self.salary}")

class Designer(Employee):
    def __init__(self,name,address, salary, tool):
        super().__init__(name,address,salary)
        self.tool=tool
    def print_detail(self):
        super().print_detail()
        print("Tool: ",self.tool)

class Developer(Employee):
    def __init__(self,name,address, salary, programmingL):
        super().__init__(name,address,salary)
        self.programmingL=programmingL
    def print_detail(self):
        super().print_detail()
        print("ProgrammingL :",self.programmingL)

D1 = Developer(name="Dipesh",address="Kathmandu",salary=50200,programmingL="Python")
D1.print_detail()
De1 = Designer(name="surya",address="Kathmandu",salary=11000,tool="figma")
De1.print_detail()


#its good to know this