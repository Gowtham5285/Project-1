# try:
#     a=[1,2,3]
#     print(a[4])
# except IndexError:
#     print("Array index out of bound")
# else:
#     print("Correct way of execution")
# finally:
#     print("execution done")
# def divide(a,b):
#     if b==0:
#         raise ZeroDivisionError("Value must be greater than zero")
#     else:
#         print(a//b)
# print(divide(2,3))
# print(divide(2,0))

# try:
#     x = int("abc")
# except ValueError:
#     print("Invalid input, raising again...")
#     raise   # re-throws the same error
# username = ""

# if username == "":
#     raise Exception("Username cannot be empty")
# balance = 5000

# try:
#     amount = int(input("Enter amount to withdraw: "))
#     if amount > balance:
#         raise ValueError("Insufficient Balance")
# except ValueError as e:
#     print("Transaction Error:", e)
# else:
#     balance -= amount
#     print("Withdrawal Successful!")
# finally:
#     print("Thank you for using the ATM.")

# bal=5000
# try:
#     amount=int(input("Enter the amount to withdraw:"))
#     if amount>bal:
#         raise ValueError("Insufficient Balance")
# except ValueError as e:
#     print("Incomplete Transaction:",e)
# else:
#     bal-=amount
#     print("Amount Successfully Withdrawn")
# finally:
#     print("Thank you for using ATM")
age = 15
assert age >= 18, "Age must be 18+"
