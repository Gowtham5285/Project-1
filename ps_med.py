# s1=input("Enter the string:-")
# l1=[]
# d1={}
# for i in s1:
#     l1.append(i)
# for i in set(l1):
#     if l1.count(i)>0:
#         d1[i]=l1.count(i)
# for i,j in d1.items():
#     print(i,j,end="",sep="")
a="swiss"
l1=[]
for i in a:
    l1.append(i)
print(l1)
for i in set(l1):
    if l1.count(i)==1:
        print(i)
        break