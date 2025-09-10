# Why do we need oops language:-
# Modularity & organization
# Code reusability
# Data Hiding & Encapsulation
# Building Real World entities
# Maintability & Scalability
# Everything in python is object
import requests
apiUrl="https://fakestoreapi.com/products"
response=requests.get(apiUrl)
# print(response)
class fakeStoreProduct:
    def __init__(self,t,i,p):
        self.title=t
        self.image=i
        self.price=p
    def ProductDetails(self):
        print(f"{self.title} and the price is {self.price}")

if response.status_code==200:
    data=response.json()
    # print(data)
    for i in data:
        title=i["title"]
        image=i["image"]
        price=i["price"]
        abc=fakeStoreProduct(title,image,price)
        abc.ProductDetails()
