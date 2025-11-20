# n=int(input("enter a number: "))
# if(n%2==0):
#     for i in range(n,0,-1):
#         if i%2==0:
#             print("*"*i,end="")
#         else:
#             continue
#         print()
# else:
#     for i in range(n,0,-1):
#         if i%2==1:
#             print("*"*i,end="")
#         else:
#             continue
#         print()
# name="gowtham"
# half=len(name)//2
# first_half=name[:half]
# second_half=name[half:]
# uppercase_char=""
# for i in second_half:
#     if 'a'<=i<='z':
#         uppercase_char=chr(ord(i)-32)  
#         first_half+=uppercase_char
#     else:
#        uppercase_char=i
#        first_half+=uppercase_char
# print(first_half)
# a=5
# print(a<<1)#left shift
# print(a>>1)#right shift
# class Parent:
#     def func1(self):
#         print("This is parent class")
# class Child(Parent):
#     def func2(self):
#         print("This is child class")
# class GrandChild(Child):
#     def func3(self):
#         print("This is grandchild class")
# g=GrandChild()
# g.func1()
# g.func2()
# g.func3()

num=1234
digit=0
product=1
while num>0:
    digit=num%10
    product=product*digit
    num=num//10
print(product)
