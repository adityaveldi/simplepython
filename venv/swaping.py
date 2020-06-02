a=int(input('Enter the fist value:'))
b=int(input('Enter the second value:'))
print('Before swapping a={} and b={}'.format(a,b))
a=a+b
b=a-b
a=a-b
print('After swapping a={} and b={}'.format(a,b))
