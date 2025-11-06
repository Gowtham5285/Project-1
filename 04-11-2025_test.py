class Bank:
    def __init__(self,name,ibalance,pin):
        self.name=name
        self.iblance=ibalance
        self.__pin=pin
        self.accountStatus=True
        self.ATMcardrequestStatus=False
        self.CheckBookrequestStatus=False


    def __Pincheck(self,pin):
        return self.__pin==pin
        
    def checkBalance(self,pin):
        if self.accountStatus:
            if self.__Pincheck(pin):
                print(f"The balance is {self.iblance}")
            else:
                print("Incorrect PIN")
        else:
            print("Your account is not in active. Please try to activate it")

    def __removeAmount(self,amount):
        if amount<=self.iblance:
            self.iblance-=amount
            print(f"The amount {amount} is withdrawed. the balance is {self.iblance}")
        else:
            print("The amount is exceeded to the balance")

    def withdrawFunds(self,pin,amount):
        if self.accountStatus:
            if self.__Pincheck(pin):
                self.__removeAmount(amount)
            else:
                print("You entered the wrong pin")
        else:
            print("Your account is not in active. Please try to activate it")

    def __Addamount(self,addamount):
        if addamount>0:
            self.iblance+=addamount
            print(f"The amount {addamount} is added. The balance is {self.iblance}")
        else:
            print("add amount greater than 0")

    def DepositFunds(self,pin,addamount):
        if self.accountStatus:
            if self.__Pincheck(pin):
                self.__Addamount(addamount)
            else:
                print("you entered the wrong pin")
        else:
            print("Your account is not in active. Please try to activate it")


    def ATMcardrequest(self):
        if self.accountStatus:
            if self.ATMcardrequestStatus==False:
                self.ATMcardrequestStatus=True
                print("The ATM card Request is accepted. Please wait for Sometime to get the ATM card")
            else:
                print("you already had an ATM card")
        else:
            print("Your account is not in active. Please try to activate it")

    def Checkbookrequest(self):
        if self.accountStatus:
            if self.CheckBookrequestStatus==False:
                self.CheckBookrequestStatus=True
                print("Your checkbook Status is approved")
            else:
                print("you already had a check book request")
        else:
            print("Your account is not in active. Please try to activate it")
    def freezeAccount(self):
        if self.accountStatus==False:
            print("yor account is already freezed")
        else:
            self.accountStatus=False
            print("your account is going to be freezed")

    def UnfreezeAccount(self):
        if self.accountStatus==False:
            self.accountStatus=True
            print("yor account is going to be Unfreezed")
        else:
            print("your account is in active")

class Savings(Bank):
    def __init__(self,name,ibalance,pin):
        super().__init__(name,ibalance,pin)
class Business(Bank):
    def __init__(self,name,ibalance):
        self.name=name
        self.ibalance=ibalance
    def showBalance(self,pin):
        super().checkBalance(pin)
savingsuser=Savings("Ram",1300,1234)
savingsuser.checkBalance(1234)
savingsuser.withdrawFunds(1234,1200)
savingsuser.DepositFunds(1234,300)
savingsuser.ATMcardrequest()
businessuser=Business("cotton",50000)
businessuser.showBalance(1234)