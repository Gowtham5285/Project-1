# import requests
# apiUrl="https://jsonplaceholder.typicode.com/users"
# response=requests.get(apiUrl)

# class User:
#     def __init__(self,id,name,email):
#         self.id=id
#         self.name=name
#         self.email=email

#     def showUser(self):
#         print(f"User #{self.id} -> {self.name} ({self.email})")

#     def getEmailDomain(self):
#         return self.email.split('@')[-1]

# if response.status_code==200:
#     data=response.json()
#     user_objects=[User(u["id"], u["name"], u["email"]) for u in data]

#     for i in user_objects[:5]:
#         i.showUser()
#         print("Domain:",i.getEmailDomain())
# else:
#     print("Failed to fetch data from API")



# import requests
# apiUrl="https://jsonplaceholder.typicode.com/posts"
# response=requests.get(apiUrl)

# class Post:
#     def __init__(self,ui,i,t,b):
#         self.userid=ui
#         self.id=i
#         self.title=t
#         self.body=b

#     def showSummary(self):
#         print(f"Post #{self.id} → {self.title[:20]}...")

#     def getWordCount(self):
#         return len(self.body.split())

# if response.status_code==200:
#     data=response.json()
#     post_objects = [Post(p["userId"], p["id"], p["title"], p["body"]) for p in data]

#     for post in post_objects[:3]:
#         post.showSummary()
#         print("Word Count:", post.getWordCount())
# else:
#     print("Failed to fetch data from API")




# import requests

# class Product:
#     def __init__(self, id, title, price, stock):
#         self.id = id
#         self.title = title
#         self.price = price
#         self.stock = stock

#     def showDetails(self):
#         print(f"{self.title} (₹{self.price}) – Stock: {self.stock}")

#     def buyProduct(self, qty):
#         if qty <= self.stock:
#             self.stock -= qty
#             total_cost = qty * self.price
#             print(f"Bought {qty} x {self.title} → Total: ₹{total_cost}")
#         else:
#             print(f"{self.title}: Out of stock (Requested {qty}, Available {self.stock})")


# url = "https://dummyjson.com/products"
# response = requests.get(url)

# if response.status_code == 200:
#     products_data = response.json()["products"]
#     product_objects = [Product(p["id"], p["title"], p["price"], p["stock"]) for p in products_data]
#     print("Available Products:")
#     for prod in product_objects:
#         prod.showDetails()

#     product_objects[0].buyProduct(2)
#     product_objects[1].buyProduct(1)   
#     product_objects[2].buyProduct(9999) 

# else:
#     print("Failed to fetch products")
