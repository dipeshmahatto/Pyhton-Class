from employee import Employee;

class Designer(Employee):
    def __init__(self,name,address, salary, tool):
        super().__init__(name,address,salary)
        self.tool=tool
    def print_detail(self):
        super().print_detail()
        print("Tool: ",self.tool)