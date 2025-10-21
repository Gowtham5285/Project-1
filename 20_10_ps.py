#1
# a=101
# sum=0
# for i in str(a):
#     sum+=int(i)
# print(sum)
#2
# a=1245
# b=a
# rev=0
# rem=0
# while a>0:
#     rem=a%10
#     rev=rev*10+rem
#     a=a//10
# print(rev)
#3
# a=5
# fact=1
# while a>0:
#     fact=fact*a
#     a-=1
# print(fact)
# 4
# a="world"
# l=len(a)//2
# if l%2==0:
#     print(a[l])
# else:
#     print(a[l-1:l+1])
# 5
# a=75547
# b=str(a)
# sum=0
# c=int(b[-1])+int(b[0])
# d=str(b[1:len(b)-1])
# for i in d:
#     sum=sum+int(i)
# if sum==c:
#     print("equal")
# else:
#     print("not equal")
# 6
# a=84719 
# l1=[]
# rem=0
# while a>0:
#     rem=a%10
#     l1.append(rem)
#     a=a//10
# for i in l1:
#     if 
# 7
# a="HelloWorld"
# s1=""
# for i in a:
#     if i in "aeiouAEIOU" and i not in s1:
#         s1+=i
#     else:
#         continue
# print(s1)
# 8
# a="donkey"
# b=""
# for i in a:
#     if a.count(i)==1:
#         b+=i
# print(b)
# 9
# a="HelloJack"
# b=""
# for i in a:
#     if i.isupper():
#         b+=i.lower()
#     elif i.islower():
#         b+=i.upper()
#     else:
#         continue
# # print(b)
# 10
# a="HelloJack"
# b=[]
# for i in a:
#     if i.isupper():
#         b.insert(0,i)
#     else:
#         b.append(i)
# print(b)
# c="".join(b)
# print(c)
# 11
# a= [3, 1, 4, 1, 5, 9] 
# larg=0
# for i in a:
#     if i>larg:
#         larg=i
# print(larg)
# 12
# a=[3, 1, 4, 1, 5, 9]
# first=0
# second=0
# for i in a:
#     if i>first:
#         second=first
#         first=i
#     elif first>i>second:
#         secnd=i
# print(second)
# a=[1,2,3,4,5]
# a.reverse()
# print(a)
# 12
# a=[0, 1, False, 2, '', 3]
# b=[]
# for i in a:
#     if i==False or i=="" or i=='':
#         continue
#     else:
#         b.append(i)
# print(b)
# a=[1,2,3,4,3,2,5]
# b=[]
# for i in set(a):
#     if a.count(i)==1:
#         b.append(i)
# print(b)
# def find_permutations(s):
#     if len(s) == 1:
#         return [s]
    
#     perms = []
#     for i in range(len(s)):
#         # Take one character out
#         char = s[i]
#         # Remaining string
#         rest = s[:i] + s[i+1:]
#         print(rest)
#         # Recursive call for rest of the string
#         for perm in find_permutations(rest):
#             perms.append(char + perm)
    
#     return perms

# # Testcase
# print(find_permutations("abcd"))
def roman_to_int(a):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 
        'L': 50, 'C': 100, 
        'D': 500, 'M': 1000
    }
    total=0
    for i in range(len(a)):
        if i+1 < len(a) and roman_values[a[i]]<roman_values[a[i+1]]:
            total-=roman_values[a[i]]
        else:
            total+=roman_values[a[i]]
    return total
print(roman_to_int("VI"))
class abc:
    def __init__(self,bcd):
        self.name="Ram"
        self.bcd=bcd
class bcd:
    def __init__(self):
        self.name1="Shyam"
    def show(self):
        print("hi")
bcd1=bcd()
obj=abc(bcd1)
print(obj.bcd.show())
      
    
    
