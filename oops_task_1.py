# class restauraunt:
#     def __init__(self,r,m):
#         self.restaurant=r
#         self.menu=m

#     def showMenu(self):
#         print(f"---------The {self.restaurant} menu-----------")
#         for item, price in self.menu.items():
#             print(f"{item} - ${price}")

#     def orderFood(self,item,qty):
#         if item in self.menu:
#             total=self.menu[item] * qty
#             print(f"Order placed: {qty} x {item} = ₹{total}")
#         else:
#             print("Item not available")

# dominos=restauraunt("Dominos",{
#     "pizza":200,
#     "garlic-bread":120,
#     "pasta":150
# })
# kfc=restauraunt("KFC",{
#     "Burger":150,
#     "chicken wings":250,
#     "Fries":100
#     })

# dominos.showMenu()
# kfc.showMenu()

# dominos.orderFood("Pizza", 2)    
# dominos.orderFood("Burger", 1)    
# kfc.orderFood("Fries", 3)         
# kfc.orderFood("Pasta", 1) 


# class Driver:
#     def __init__(self,n,cn,pkr):
#         self.name=n
#         self.carName=cn
#         self.kmrate=pkr

#     def showDriver(self):
#         print(f"Driver:{self.name}, Car:{self.carName}, Rate:{self.kmrate}")

#     def calculateFair(self,distance):
#         fare= distance * self.kmrate
#         print(f"Distance:{distance}km, Fare:${fare}")

# driver1=Driver("Ram","Porsche",50)
# driver2=Driver("Shyam","Bentley",60)
# driver3=Driver("Ravi","BMW",40)

# driver1.showDriver()
# driver2.showDriver()
# driver3.showDriver()

# driver1.calculateFair(5)
# driver2.calculateFair(10)
# driver3.calculateFair(20)


class Product:
    def __init__(self,pn,p,s):
        self.Product_name=pn
        self.price=p
        self.stock=s

    def showDetails(self):
        print(f"{self.Product_name} -${self.price}, Stock:{self.stock}")

    def buyProduct(self,qty):
        if qty <= self.stock:
            total= self.price * qty
            self.stock -= qty
            print(f"Purchased {qty} x {self.Product_name} = ${total}")
            print(f"Remaining Stock of {self.Product_name}: {self.stock}")
        else:
            print(f"Out of Stock! Only {self.stock} {self.Product_name}(s) left.")

laptop=Product("Lenovo ideapad3",50000,25)
phone=Product("Realme C3",20000,5)
shoes=Product("Nike amad",5000,3)

laptop.showDetails()
phone.showDetails()
shoes.showDetails()

laptop.buyProduct(2)
phone.buyProduct(1)
shoes.buyProduct(4)