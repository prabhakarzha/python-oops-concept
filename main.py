class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name =first_name
        self.last_name =last_name
        self.age =age

p1 =Person('Sonu' ,'kashyap',22)

p2 =Person("rishu","jha",24)

print(p1.first_name)

class Laptop:
    def __init__(self,brand, name ,price):

        #instance variable
        self.brand =brand
        self.name =name
        self.price =price
laptop1 =Laptop('hp','au114tx',65000)
print(laptop1.name)

