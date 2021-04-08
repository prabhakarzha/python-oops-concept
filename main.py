# class Person:
#     def __init__(self,first_name,last_name,age):
#         self.first_name =first_name
#         self.last_name =last_name
#         self.age =age

# p1 =Person('Sonu' ,'kashyap',22)

# p2 =Person("rishu","jha",24)

# print(p1.first_name)

# class Laptop:
#     def __init__(self,brand, name ,price):

#         #instance variable
#         self.brand =brand
#         self.name =name
#         self.price =price
# laptop1 =Laptop('hp','au114tx',65000)
# print(laptop1.name)



class Student:
    def check_pass_fail(self):
        if self.marks>=40:
            return True
        else:
            return False

    def __init__(self,name,marks):
        self.name =name
        self.marks =marks


student1 =Student("sonu",85)
print(student1.name)
print(student1.marks)






