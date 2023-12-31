class BankAccount:
    def __init__(self,name,address,acc_number,balance) -> None:
        self.__name = name
        self.__address = address
        self.__acc_number=acc_number
        self.__balance = balance
    
    def acc_details(self):
        print(f"Account holder name is {self.__name} , Address is {self.__address} and Account number is {self.__acc_number} with Balance : {self.__balance}")
    
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance= self.__balance-amount
            print(f"{amount} is sucessfully withdraw form Account : {self.__acc_number} and Name : {self.__name}")
            print(f"Remaining Balance : {self.__balance}")
        else :
            print("Insufficent balance !!!")

    def deposite(self,amount):
        self.__balance=self.__balance+amount
        print(f"{amount} is sucessfully deposited to Account : {self.__acc_number} and Name : {self.__name}")
        print(f"Account Balance :{self.__balance}")

bankaccount = BankAccount("Dipesh Mahato","Kathmandu",17485461878,10000)
bankaccount.acc_details()
bankaccount.withdraw(5000)
bankaccount.deposite(2000)