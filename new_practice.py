#1
# a = 300
# c1 = a // 1000     
# a = a % 1000
# c2 = a // 500       
# a = a % 500
# if a != 0:
#     print(f"1000s are {c1}, 500s are {c2}, remaining value is {a}")
# else:
#     print(f"1000s are {c1}, 500s are {c2}")

# seconds = int(input("Enter total seconds: "))

# hours = seconds // 3600          
# seconds = seconds % 3600

# minutes = seconds // 60          
# seconds = seconds % 60

# print(f"{hours} hour(s), {minutes} minute(s), and {seconds} second(s)")


# year = int(input("Enter a year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is a Leap Year")
# else:
#     print(f"{year} is Not a Leap Year")

# n = int(input("Enter number of rows: "))

# for i in range(n):
#     num = 1
#     for j in range(i + 1):
#         print(num, end=" ")
#         num = num * (i - j) // (j + 1)
#     print()


# n = 7  

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if (
#             j == 1                       
#             or j == n                    
#             or j == i                    
#             or j == (n - i + 1)           
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = 7

# for i in range(1, n + 1):
#     for j in range(1, 6):
#         if (
#             i == 1 or i == n or                  # top & bottom border
#             (i == 2 and (j == 1 or j == 5)) or   # 2nd row sides only
#             (i - j == 2) or                      # left diagonal
#             (i + j == 8)                         # right diagonal
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#area of square
# s=5
# a=s*s
# print(a)

#Area of rectangle
# l=5
# b=6
# areaofr=l*b
# print(areaofr)

#Area of triangle
# he=6
# br=8
# areaofTr=0.5*(he*br)
# print(areaofTr)

#perimeter of square
# si=6
# print(4*si)

#Perimeter of rectangle
# length=4
# breadth=9
# print(2*(length+breadth))

#perimeter of triangle
# side1=4
# side2=33
# side3=9
# print(side1+side2+side3)

# a=0
# b=1
# for i in range(10):
#     print(a,end=" ")
#     a,b=b,a+b
# print()
# n=5
# for i in range(1,n+1):
#     # print(" "*(n-i),end="")
#     for j in range(n,i-1,-1):
#         print(j+1,end="")
#     print()
matrix = [[1, 2], [3, 4]]
diag = [matrix[i][i] for i in range(len(matrix))]
print(diag)  # Output: [1, 4]
