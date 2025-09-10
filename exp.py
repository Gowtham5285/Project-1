class Product:
    def __init__(self,pn,p,s):
        self.Product_name=pn
        self.price=p
        self.stock=s

    def showDetails(r):
        print(f"{r.Product_name} -${r.price}, Stock:{r.stock}")

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