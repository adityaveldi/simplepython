# If a number is said to be prime it has only 2 factors they are 1 and it self
num=int(input('Enter the number:'))
count=1
for x in range(2,num):
    if(num%x==0):
        count+=1
    else:
        continue

if(num==1 or num==0):
    print('given number ',num,' neither prime nor composite')
elif(count==2):
    print('given number ',num,' is prime')
else:
    print('given number ',num,' is composite')
