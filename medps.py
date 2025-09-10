# a="rama"
# mid=len(a)//2
# b=a[:mid]
# c=a[mid:]
# c1=0
# c2=0
# for i in b:
#     if i in "aeiouAEIOU":
#         c1+=1
# for i in c:
#     if i in "aeiouAEIOU":
#         c2+=1
# if c1==c2:
#     print("true")
# else:
#     print("false")
# a=[22,34,25,121,346]
# c=0
# for i in a:
#     s=str(i)
#     if s[0]==s[-1]:
#         c+=1
#     else:
#         pass
# print(c)
# a=[7,4,7,23,10]
# res=[]
# for i in a:
#     b=i+1
#     c=0
#     for j in range(2,b):
#         if b%j==0:
#             c+=1
#     if c==0:
#         res.append(i)
# print(*res,sep=" ")
# a= [ 61, 4, 6, 7, 120 , 10 ]
# b=5
# fact=1
# for i in range(1,b+1):
#     fact *= i
# for i in range(len(a)):
#     if fact == a[i]:
#         print(i)
# num=12345643
# s=str(num)
# d=[]
# sum=0
# for i in set(s):
#     if s.count(i)>1:
#         d.append(i)
# print(d)
# for i in d:
#     sum+=int(i)
# print(sum)
# a="swiss"
# for i in a:
#     if a.count(i)==1:
#         print(i)
#         break
# roman={
#     'I':1,
#     'V':5,
#     'X':10,
#     'L':50,
#     'C':100,
#     'D':500,
#     'M':1000
# }
# n='LVIII'
# total=0
# prev_value=0
# for i in reversed(n):
#     value=roman[i]
#     if value<prev_value:
#         total -= value
#     else:
#         total+=value
#         prev_value=value
# print(total)
# a=[141,3,4,5,6,4,5]
# b={}
# for i in set(a):
#     if a.count(i)>1:
#         b[i]=a.count(i)
# if len(b) >= 2:
#     second_key = list(b.keys())[1]
#     print(second_key, ":", b[second_key])
# n=4
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# n=int(input("number:- "))
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print(j,end="")
#     print()
# for i in range(1,n+1):
#     s=0
#     for j in range(1,i+1):
#         print(j,end=" ")
#         s+=j
#     print(s)
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("+" * i)
# for i in range(1,n+1):
#     print("+" * i,end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# n = int(input("Enter number of rows: "))

# for i in range(1, n+1):
#     # print letters (A, B, C, ...)
#     for j in range(65, 65+i):   # ASCII of 'A' = 65
#         print(chr(j), end="")
#     # print numbers
#     for k in range(1, i+1):
#         print(k, end="")
#     print()
# a=[1,2,3]
# b=[1,2,4]
# c=[]
# for i in range(len(a)):
#     if a[i]==b[i]:
#         c.append(a[i])
# print(c)
# def reverse_words(s):
#     words = s.split()          # split by spaces into list of words
#     reversed_words = words[::-1]  # reverse the list
#     return " ".join(reversed_words)
# print(reverse_words("the sky is blue"))   # "blue is sky the"
# print(reverse_words("hello world"))
