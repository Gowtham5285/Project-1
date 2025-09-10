class Order:
    def __init__(self,oi,i,a):
        self.orderid=oi
        self.items=i
        self.amount=a

    def show_Order(self):
        tax=50
        print(f"The order id is {self.orderid} & the items are {self.items} and the amount is {self.amount} & the tax is {tax + self.amount}")

class Delivery(Order):
    def show_Delivery(self):
        super().show_Order()
        print("Delivery Status: Out for delivery")

order1=Delivery(101,["Milk","Bread","Eggs"],250)
order1.show_Delivery()


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def show_product(self):
        platform = "Amazon"
        print(f"Product Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ₹{self.price}")
        print(f"Available On: {platform}")


class DiscountedProduct(Product):
    def show_discount(self, discount_percentage):
        super().show_product()
        final_price = self.price - (self.price * discount_percentage / 100)

        print(f"Discount: {discount_percentage}%")
        print(f"Final Price after Discount: ₹{final_price}")


product1 = DiscountedProduct("Laptop", 60000, "Electronics")
product1.show_discount(10)


class Ride:
    def __init__(self,ride_id,pickup,drop):
        self.ride_id = ride_id
        self.pickup = pickup
        self.drop = drop

    def show_ride(self):
        distance=12
        print(f"Ride id: {self.ride_id}")
        print(f"Pickup Location: {self.pickup}")
        print(f"Drop Location: {self.drop}")
        print(f"Distance: {distance}")


class Driver(Ride):
    def show_driver(self):
        super().show_ride()
        print("Driver Status: Arriving Soon 🚘")


ride1=Driver(501,"MG Road","Airport")
ride1.show_driver()
