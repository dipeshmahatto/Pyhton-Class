class Student:
    def __init__(self,id,name,address,ph_no):
        self.id=id
        self.name=name
        self.address=address
        self.ph_no = ph_no

    def print_details(self):
        print(f"ID : {self.id} Name : {self.name} Address : {self.address} PhoneNumber : {self.ph_no}")

# student1 = Student()
# print("Name :",student1.name)
# print("ID :",student1.id)
# print("Address :",student1.address)
# student1.print_details()
        
student1 = Student(1,"Ram","ktm",9803643491)
student1.print_details()