class parent:
    def add():
        print('This is parent class')
class riding(parent):
    def add():
        print('This is child class')
cls=parent
cls.add()
cls=riding
cls.add()