# generating multiplication table for the given value
num=int(input('Enter the value:'))
for x in range(1,11):
    print('',num,' * ',x,' = ',(num*x))
