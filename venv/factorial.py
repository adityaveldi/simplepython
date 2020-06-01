# wrting the program to find the factorial of the number
value=int(input('enter the value you want to find the factorial:'))
fact=1
for x in range(2,value+1):
    fact=fact*x

print('the factorial is:',fact)