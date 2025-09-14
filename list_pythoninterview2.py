# a=[1,2,3,4]
# b=[3,4,5,6]
# c=[]
# for i in a+b:
#     if i not in c:
#         c.append(i)
# print(c)
# a=[10, 15, 20, 25, 30]
# even=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)
# a= [1, 2, 3, 7, 8, 9]
# sum=10
# for i in range(len(a)):
#     for j in range(len(a)):
#         if sum==a[i]+a[j]:
#             print(a[i],a[j])
# a = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in a:
#     if i > 1:
#         for j in range(2, i): 
#             if i % j == 0: 
#                 break
#         else:
#             print(i)
a = [12, 45, 2, 7, 23, 5]
smallest = float('inf')
second_smallest = float('inf')
for num in a:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif smallest < num < second_smallest:
        second_smallest = num
print("Second smallest:", second_smallest)

            
            