class Parent:
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def display(self):
        print('you are graduated in :',self.year)

class Child(Parent):
    def __init__(self,name,year):
        super().__init__(name,year)


obj=Child('aditya',2021)
obj.display()
