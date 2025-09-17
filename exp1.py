
class HDFCBankAccount:
    def _init_(self,user_name,main_bal,pin=1234):
        self.name=user_name
        self.__MainBal=main_bal
        self.__pin=pin
        self.__account_Acrive_Status=True
        self.__isAtmCardHolder=False
        self.__isCheckBookHolder=False
        self.__isAtmCardGotFreezed=False
    
    def __verifyPin(self,pin):
        return self.__pin==pin
        
    def __updateMainBalByWithDraw(self,amount):
        self.__MainBal -=amount
        print(f"you have drawn {amount} successfully,",self.__MainBal, "is main bal")
        
    def __updateMainBalByDeposit(self,amount):
        self.__MainBal +=amount
        print(f"you have credited {amount} successfully to yr own account,",self.__MainBal, "is main bal")    
    
    def __show_MainBal(self):
        print(f"{self.__MainBal} is main bal")
    
    def __raiseAtmCard(self):
        self.__isAtmCardHolder=True
        return f"atm card approved"
    
    def __raiseCheckBook(self):
        self.__isCheckBookHolder=True
        return f"check book approved"
    
    def __ATMCardFreezing(self):
        self.__isAtmCardGotFreezed=True
        return f"atm card got freezed"
        
        
        
    def withdraw(self,amount,pin):
        if self.__account_Acrive_Status:
            if self.__verifyPin(pin):
                if amount > self.__MainBal:
                    print("you are trying draw more amount than yr main abal")
                else:
                    self.__updateMainBalByWithDraw(amount)
            else:
                print("incorrect pin...")
                
    def deposit(self,amount,pin):
        if self.__account_Acrive_Status:
            if self.__verifyPin(pin):
                self.__updateMainBalByDeposit(amount)
            else:
                print("incorrect pin")
        else:
            print("yr account is not active in status")
    
    def check_Bal(self,pin):
        if self.__account_Acrive_Status:
            if self.__verifyPin(pin):
                self.__show_MainBal()
    
                
    
    # def mini_States(self):
    #     pass
    
    def request_for_ATMCard(self):
        statusOfAtmCardApproval=self.__raiseAtmCard()
        print(statusOfAtmCardApproval)
    
    def request_for_CheckBook(self):
        statusOfCheckBookApproval=self.__raiseCheckBook()
        print(statusOfCheckBookApproval)
    
    def request_for_ATMCardFreezing(self):
        print(self.__ATMCardFreezing())
    
    def request_for_AccountFreezing(self):
        pass

class SavingAccount(HDFCBankAccount):
    def _init_(self,name,bal):
        self.loanLimit=300000 #insta var of SavingAcc
        super()._init_(name,bal)
    def personalLoanRaise(self,amount):
        if amount >self.loanLimit:
            print("you are exceeding yr loan limit amount")
        else:
            print("you are quoting in yr loan limit amount.... you will granted loan soon")
    
class BusinessAccount(HDFCBankAccount):
    def _init_(self,name,bal):
        self.loanLimit=2000000 #insta var of SavingAcc
        super()._init_(name,bal)
    def businessLoanRaise(self,amount):
        if amount >self.loanLimit:
            print("you are exceeding yr loan limit amount")
        else:
            print("you are quoting in yr loan limit amount.... you will granted loan soon")
        

sAccount=SavingAccount("vamsi",50000)
bAccount=BusinessAccount("rakesh",1000000)
amount=int(input("enter amount :-   "))
# pin=int(input("enter pin :-- "))
# sAccount.personalLoanRaise(amount)
bAccount.businessLoanRaise(amount)
# sAccount.request_for_ATMCard()
# sAccount.request_for_CheckBook()
# sAccount.request_for_ATMCardFreezing()
# sAccount.withdraw(amount,pin)
# sAccount.deposit(amount,pin)
# sAccount.check_Bal(pin)