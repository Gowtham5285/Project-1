class Bank:
    def __init__(self,name,initbal,pin):
        self.name=name
        self.initialbalance=initbal
        self.pinnumber=pin
        self.accountstatus=True
        self.ATMcardStatus=False
        self.CheckBookStatus=False
    
    def __pin(self,pinnumber):
        return 1234==pinnumber
    
    def showBalance(self):
        if self.accountstatus:
                    
                    if self.__pin(self.pinnumber): 
                         print(f"The balance is {self.initialbalance}")
                    else:
                        print("The pin you entered was wrong")
        else:
             print("Your account is not active")

    def __balance(self,amount):
         self.initialbalance=self.initialbalance-amount
         print("The balance is:-", self.initialbalance)
    
    def withdrawFunds(self,amount,pin):
         if self.accountstatus:
              if self.__pin(pin):
                   if amount>self.initialbalance:
                        print("Don't exceed the balance limit")
                   else:
                        self.__balance(amount)
              else:
                   print("Enter the right PIN")
         else:
              print("Your account  status is not active")

    def __Addbalance(self,amount):
         self.initialbalance+=amount
         print("The amount is credited, the main balance is:",self.initialbalance)
                   
    def depositFunds(self,amount,pin):
        if self.accountstatus:
              if self.__pin(pin):
                   if amount>self.initialbalance:
                        print("Don't exceed the balance limit")
                   else:
                        self.__Addbalance(amount)
              else:
                   print("Enter the right PIN")
        else:
              print("Your account  status is not active")

    def __ATMcardrequest(self):
         if self.ATMcardStatus==True:
              print("You already had a ATM card")
         else:
              self.ATMcardStatus=True
              print("Your request approved")

    def atmCardRequest(self):
         self.__ATMcardrequest()

    def __CheckBookrequest(self):
         if self.CheckBookStatus==True:
              print("You already requested the checkbook")
         else:
              self.CheckBookStatus=True
              print("Request will approved within a day")

    def chequeBookRequest(self):
         self.__CheckBookrequest()

    def __accountStatus(self):
         if self.accountstatus==False:
              print("Already the account is freezed")
         else:
              self.accountstatus=False
              print("The account is freezed")

    def freezeAccount(self):
         self.__accountStatus()

    def __unfreezeAccount(self):
        if self.accountstatus==True:
              print("Already the account is Active")
        else:
              self.accountstatus=True
              print("The account is Active now") 

    def unfreezeAccount(self):
         self.__unfreezeAccount()


class Savings(Bank):
     def __init__(self,name,initbal,pin):
          super().__init__(name,initbal,pin)
class Business(Bank):
    def __init__(self):
        pass
# name=input("enter the name of account:")
# initbalance=int(input("enter the initial balance"))
# pinnum=int(input("enter the 4 digit pin number"))
obj1=Savings("ram",1300,1234)
# obj1.showBalance()
obj1.withdrawFunds(1200,1234)
