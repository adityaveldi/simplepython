# now we shall see hoe to make use of loops to print a pattern in python
value=int(input("Enter the value"))
for i in range(value+1):
    for j in range(i):
        print("*",end=' ')

    print(end='\n')