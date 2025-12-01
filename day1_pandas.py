import pandas as pd
# a=pd.Series([100,400])
# print(a)
abc=pd.DataFrame([("Ram",77,9000),("shyam",77,9999)],columns=["name","age","salary"])
print(abc)
# cde=pd.DataFrame({"name":"ram","age":34},{"name":"Shyam","age":22})
# print(cde)
efg=pd.DataFrame({"id":[1,2,3],"name":["Ram","john","Eren"]},index=[1,2,3])
print(efg)

df_students = pd.DataFrame({
    "ID": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    "Name": ["Ram","Shyam","Sita","Gita","Mohan","Rohan","Sohan","Radha","Krishna","Vijay",
             "Ajay","Deepak","Aman","Ravi","Virat","Rohit","Karan","Arjun","Kabir","John"],
    "Age": [18,19,20,21,22,18,19,20,21,22,18,19,20,21,22,18,19,20,21,22],
    "Marks": [80,75,90,85,70,88,78,92,65,81,73,89,76,84,67,95,72,86,74,83],
    "City": ["Mumbai","Delhi","Pune","Chennai","Kolkata","Mumbai","Delhi","Pune",
             "Chennai","Kolkata","Mumbai","Delhi","Pune","Chennai","Kolkata",
             "Mumbai","Delhi","Pune","Chennai","Kolkata"]
})

print("Student DataFrame:\n", df_students)

df_products = pd.DataFrame({
    "Product_ID": [201,202,203,204,205,206,207,208,209,210,
                   211,212,213,214,215,216,217,218,219,220],
    "Product_Name": ["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10",
                     "P11","P12","P13","P14","P15","P16","P17","P18","P19","P20"],
    "Category": ["Electronics","Furniture","Clothing","Food","Stationery",
                 "Electronics","Furniture","Clothing","Food","Stationery",
                 "Electronics","Furniture","Clothing","Food","Stationery",
                 "Electronics","Furniture","Clothing","Food","Stationery"],
    "Stock": [50,60,70,80,90,55,65,75,85,95,52,62,72,82,92,57,67,77,87,97],
    "Price": [200,250,300,150,100,210,260,310,160,110,220,270,320,170,120,
              230,280,330,180,130]
})

print("\nProduct DataFrame:\n", df_products)

df_employees = pd.DataFrame({
    "Emp_ID": [101,102,103,104,105,106,107,108,109,110,
               111,112,113,114,115,116,117,118,119,120],
    "Name": ["A","B","C","D","E","F","G","H","I","J",
             "K","L","M","N","O","P","Q","R","S","T"],
    "Department": ["IT","HR","Finance","Marketing","Admin",
                   "IT","HR","Finance","Marketing","Admin",
                   "IT","HR","Finance","Marketing","Admin",
                   "IT","HR","Finance","Marketing","Admin"],
    "Salary": [30000,32000,35000,28000,40000,33000,36000,29000,42000,34000,
               31000,37000,30000,32500,41000,33500,38500,29500,43000,34500],
    "Experience": [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
})

print("\nEmployee DataFrame:\n", df_employees)
