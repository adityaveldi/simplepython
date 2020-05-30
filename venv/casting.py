# casting is nothing but conversion of one datatype to another data type.let us see how it will work
# basically there are the methods to cast they are int(),float() and str()
# here we are converting into int type so this may lead to loss of information this is also called as down-casting
x=int(2.3)
print(type(x),x)
x=int('23')
print(type(x),x)
# now we are converting into float value this also called as up-casting we dont lose any data here
x=float(25)
print(type(x),x)
x=float('2.3')
print(type(x),x)
# now we are converting into string type
x=str(2)
print(type(x),x)
x=str(2.3)
print(type(x),x)
# nesting of methods
x=int(float('2.3'))
print(type(x),x)
