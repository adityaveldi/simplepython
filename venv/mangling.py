class Test:
    __name='aditya'# name mangling
    city='Hyd'

c1=Test()
c2=Test()
print(c1.city)
print(dir(c1))
print(c1._Test__name)
c1.__class__.city='Knr'# __class__ used to change the class members value
print(c1.city)
print(c2.city)
c1.city='nlg'
print(c1.city)
print(c2.city)


# this mangling is used to avoid naming conflicts in the parent and its child classes.