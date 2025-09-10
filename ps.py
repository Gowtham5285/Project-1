# Write a program to print the sum of the digits in the number
# n=int(input("Number:"))
# s1=str(n)
# sum=0
# for i in s1:
#     sum+=int(i)
# print(sum)
# Write a program to print reverse of the given number. 
# n=int(input("Number:"))
# s1=str(n)
# s1=int(s1[::-1])
# print(s1) 
#Write a program to print factorial of the number. 
# n=int(input("Number:"))
# fact=1
# for i in range(2,n+1):
#     fact*=i
# print(fact)
# Write a program to print middle character(s) in the given string or number.
# str1=input("enter a string:")
# middle=len(str1)//2
# if len(str1)%2==0:
#     print(str1[middle-1:middle+1])
# else:
#     print(str1[middle])
# Write a program to check whether the sum of digits in the number except
# first digit and digit is equal to the sum of first digit and last digit of that
# number. If both the sums are equal then print equal otherwise print not
# equal
# n1=int(input("Number:"))
# n2=str(n1)
# edsum=int(n2[0])+int(n2[-1])
# sum=0
# for i in range (1,len(n2)-1):
#     sum += int(n2[i])
# if sum==edsum:
#     print("equal")
# else:
#     print("not equal")
# Write a program to check whether the digits in-between the first and last
# digit are less than first and last digit, if yes then print true, otherwise print
# false.
# str1=input("enter a number")
# fd=int(str1[0])
# ld=int(str1[-1])
# c=0
# for i in range(1,len(str1)-1):
#     if int(str1[i]) < fd and int(str1[i]) < ld:
#         c+=1
#     else:
#         c=0
# if len(str1)-2 == c:
#     print("True")
# else:
#     print("false")
# Write a program to print the vowels in the given string in reverse order
# str1=input("enter the string:- ")
# vowelRev=""
# for i in range(len(str1)):
#     if str1[i] in "aeiouAEIOU":
#         vowelRev += str1[i]
# print(vowelRev[::-1])
# Write a program to print the vowels in the given string and repeated
# vowel should be printed only single time.
# str1=input("enter the string:- ")
# vowel=""
# for i in range(len(str1)):
#     if str1[i] in "aeiouAEIOU":
#         if str1[i] not in vowel:
#             vowel += str1[i]
# print(vowel)
# Write a program to print the string after removing the duplicate characters
# in the string.
# str1=input("enter the text:- ")
# ch=""
# for i in str1:
#     if str1.count(i)==1:
#         ch += i
# print(ch)
# list1=[1,2,3,4,2,4,5]
# print(set(list1))
# s=[1,2,3,7,66,55]
# s.pop(s.index(max(s)))
# print(max(s))
# nums = [10, 20, 4, 45, 99]

# first = second = float('-inf')
# for n in nums:
#     if n > first:
#         second = first
#         first = n
#     elif n > second and n != first:
#         second = n

# print("Second largest number is:", second)
# Write a program to convert all the upper case letters in the given string to
# lower case letter and vice versa.
# s=input("enter a string")
# a=""
# for i in s:
#     if i.isupper():
#         a += i.lower()
#     else:
#         a += i.upper()
# print(a)
# Write a program to print all the Upper case letters in the string in reverse
# order and then followed by the lower case letters .
# s=input("enter a string")
# a=""
# b=len(s)
# for i in range(b-1,-1,-1):
#     if s[i].isupper():
#         a += s[i]
# for i in s:
#     if i.islower():
#         a += i
# print(a)
a=[1,6,5,3,4]
for i in range(len(a)-1):
    if a[i] > a[i-1]:
        print("not sorted")
    else:
        print("sorted")