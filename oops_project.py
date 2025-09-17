class HDFCBankAccount:
    def __init__(self,username,main_bal):
        self.name=username
        self.__MainBal=main_bal
        self.__pin=1234
        self.__account_Active_Status=True
     
    def __verifyPin(self,pin):
        return self.__pin==pin
    
    def __updateMainBalance(self,amount):
        self.__MainBal-=amount
        print(f"You have sucessfully drawn {amount} the balance is {self.__MainBal}")

    def withdraw(self,amount,pin):
        if self.__account_Active_Status:
            if self.__verifyPin(pin):
                if amount>self.__MainBal:
                    print("you are tring to draw more than you have in your bank account")
                else:
                    self.__updateMainBalance(amount)
            else:
                print("incorrect pin")

    def __updateMainBalByDeopsit(self,amount):
        self.__MainBal+=amount
        print(f"you have successfully the amount {amount} the balance is {self.__MainBal}")
    
    def deposit(self,amount,pin):
        if self.__account_Active_Status:
            if self.__verifyPin(pin):
                self.__updateMainBalByDeopsit(amount)
            else:
                print("incorrect pin")
        else:
            print("Your account is not in active status")
    
    def __show_MainBal(self,pin):
        if self.__account_Active_Status:
            if self.__verifyPin(pin):
                print(f"the main balance is {self.__MainBal}")

    def __request_for_atmcard_approval(self):
        pass
    
    def request_for_AccountFreezing(self):
        pass

    def check_Bal(self,pin):
        if self.__account_Active_Status:
            if self.__verifyPin(pin):
                self.__show_MainBal(pin)

    
    def mini_States(self,Pin):
        pass
    
class SavingsAccount(HDFCBankAccount):
    def __init__(self,name,bal):
        self.loanLimit=300000 #instance variable of class
        super().__init__(name,bal)

    def personalLoanRise(self):
        pass

# class BusinessAccount(HDFCBankAccount):
#     def businessLoanRise(self):
#         pass
sAccount=SavingsAccount("Ram",10000)
amount=int(input("Enter the amount:-"))
pin=int(input("Enter the pin:-"))
sAccount.withdraw(amount,pin)
sAccount.deposit(amount,pin)