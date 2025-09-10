class Parent:
    def __init__(self,n,i,r):
        self.name=n
        self.id=i
        self.rank=r
        print("parents default method")
    def showDetails(self):
        print(f"My name is {self.name} My id is {self.id} and rank is {self.rank}")
class child(Parent):
    def __init__(self, n, i, r):
        super().__init__(n, i, r)

obj1=child("ram",21,1)
obj2=child("shyam",19,34)
obj1.showDetails()
obj2.showDetails()