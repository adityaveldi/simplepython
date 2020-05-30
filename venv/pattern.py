# now we shall see hoe to make use of loops to print a pattern in python
#in python indentation is very important
value=int(input("Enter the value"))
print('using for loop')
for i in range(value+1):
    for j in range(i):
        print("*",end=' ')
    print(end='\n')
print('\nusing while loop')
i=0
j=0
while(i <= value):
    j=0
    while(j < i):
        print("*",end=' ')
        j+=1
    i+=1
    print(end='\n')