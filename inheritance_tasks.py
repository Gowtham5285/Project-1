class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class Driver:
    def __init__(self, license_no, rating):
        self.license_no = license_no
        self.rating = rating

class UberDriver(Person, Driver):
    def __init__(self, name, contact, license_no, rating, car):
        
        Person.__init__(self, name, contact)
        Driver.__init__(self, license_no, rating)
        
        self.car = car

    def show(self):
        print(f"Name: {self.name}, Contact: {self.contact}")
        print(f"License No: {self.license_no}, Rating: {self.rating}")
        print(f"Car: {self.car}")


d1 = UberDriver("Rahul", "9876543210", "DLX12345", 4.9, "Hyundai i20")
d1.show()


class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

class DeliveryPartner(Person, Employee):
    def __init__(self, name, contact, emp_id, salary, vehicle):
        Person.__init__(self, name, contact)
        Employee.__init__(self, emp_id, salary)
        self.vehicle = vehicle

    def show(self):
        print(f"Name: {self.name}, Contact: {self.contact}")
        print(f"Employee ID: {self.emp_id}, Salary: {self.salary}")
        print(f"Vehicle: {self.vehicle}")


dp1 = DeliveryPartner("Anil", "9876543210", "BKP101", 12000, "Scooter")
dp1.show()

