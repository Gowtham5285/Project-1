# a=[10, 23, 45, 66, 78, 91]
# b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)
# a=[1,2,3,4,5]
# b=[]
# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])
# print(b)
# a=[5, 7, 5, 9, 5]
# k=5
# for i in range(len(a)):
#     if a[i]==k:
#         print(i)
# a=[1, 2, 3, 2, 4, 1, 5]
# b=[]
# for i in a:
#     if i in b:
#         continue
#     else:
#         b.append(i)
# print(b)
# a=['apple', 'banana', 'apple', 'mango', 'banana', 'apple']
# frequency={}
# for i in a:
#     if i in frequency:
#         frequency[i]+=1
#     else:
#         frequency[i]=1
# print(frequency)
# nested_list = [1, [2, 3], [4, 5], 6]
# flat_list = []
# for item in nested_list:
#     if type(item) == list:   
#         flat_list.extend(item)
#     else:                    
#         flat_list.append(item)
# print(flat_list)
# a=[12, 45, 23, 67, 34]
# max=0
# secmax=0
# for i in a:
#     if i>max:
#         secmax=max
#         max=i
#     elif max>i>secmax:
#         secmax=i
# print(secmax)
