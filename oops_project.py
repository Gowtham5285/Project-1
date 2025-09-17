class SBIBank:
    def __init__(self,name,acno):
        self.Name=name
        self.AccNo=acno
        self.__pin=1234
        self.accounStatus=True
        self.mainBal=5000000
        self.__isAtmCardHolder=False
        self.__isCheckBookHolder=False
        self.__isAtmCardGotFreezed=False
        self.__isAccountedGotFreezed=False

    def __pinValidation(self,pin):
        return self.__pin==pin
        
    def showBalance(self,pin):
        if self.accounStatus:
            if self.__pinValidation(pin):
                print(f"The main balance is {self.mainBal}")
            else:
                print("Enter the Right Pin")
        else:
            print("Active your Account")
    
    def __withdrawamount(self,amount):
        self.mainBal-=amount
        print(f"the amount is debited successfully the main balance is now {self.mainBal}")
        
    def withdraw(self,amount,pin):
        if self.accounStatus:
            if self.__pinValidation(pin):
                if amount>self.mainBal:
                    print("The amount you want is more than in the account")
                else:
                    self.__withdrawamount(amount)
            else:
                print("Enter the Right Pin")
        else:
            print("Active your Account")
        
    def __depositamount(self,amount):
        self.mainBal+=amount
        print("Amount Successfully Credited to your Account")
        print(f"The Balance is {self.mainBal}")
        
    def deposit(self,amount,pin):
        if self.accounStatus:
            if self.__pinValidation(pin):
                self.__depositamount(amount)
            else:
                print("Enter the Right Pin")
        else:
            print("Active your Account")
    
    def __raiseATMCard(self):
        self.__isAtmCardHolder=True
        return f"atmcard approved"
        
    def request_for_ATMCard(self):
        Status=self.__raiseATMCard()
        print(Status)
    
    def __raiseCheckBook(self):
        self.__isCheckBookHolder=True
        return f"Checkbook Approved"
        
    def requestCheckBook(self):
        CheckbookStatus=self.__raiseCheckBook()
        print(CheckbookStatus)
    
    def __ATMCardFreezing(self):
        self.__isAtmCardGotFreezed=True
        return f"ATM was freezed"
        
    def requestforATMCardFreezing(self):
        ATMFreezingStatus=self.__ATMCardFreezing()
        print(ATMFreezingStatus)
    
    def __AccountFreezing(self):
        self.__isAccountedGotFreezed=True
        return f"Account is freezed"
        
    def requestforAccountFreezing(self):
        AccountFreezingStatus=self.__AccountFreezing()
        print(AccountFreezingStatus)
        
class savingsUser(SBIBank):
    def __init__(self,name,acno):
        self.loanLimit=300000
        super().__init__(name,acno)
    
    def personalLoan(self,amount):
        if amount>self.loanLimit:
            print("Your wanted amount is exceed the loan limit")
        else:
            print("Loan amount is sanctioned")
            
class CurrentAccount(SBIBank):
    def __init__(self,name,acno):
        self.loanLimit=5000000
        super().__init__(name,acno)
    
    def bussinessLoan(self,amount):
        if amount>self.loanLimit:
            print("Your wanted amount is exceed the loan limit")
        else:
            print("Loan amount will be sanctioned very soon")
    
user1=savingsUser("ram",123123123)
# pin=int(input("Enter the pin:-"))
# amount=int(input("Enter the amount:-"))
# user1.showBalance(pin)
# user1.withdraw(amount,pin)
# user1.deposit(amount,pin)
user1.request_for_ATMCard()
user1.requestCheckBook()
user1.requestforATMCardFreezing()
user1.requestforAccountFreezing()
user1.personalLoan(12345)
user2=CurrentAccount("ramana",20000)
user2.requestforAccountFreezing()