from employee import Employee;

class Developer(Employee):
    def __init__(self,name,address, salary, programmingL):
        super().__init__(name,address,salary)
        self.programmingL=programmingL
    def print_detail(self):
        super().print_detail()
        print("ProgrammingL :",self.programmingL)