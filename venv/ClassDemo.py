# demo for using classes and using constructors
class MyClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('Hey welcome',self.name)

p1=MyClass('aditya',20)
print(p1.name)
print(p1.age)
# printing using a method in myclass
p1.display()
# if you want to delete the property we can make use of del
del p1.age
print('deleted age property of the myclass')
