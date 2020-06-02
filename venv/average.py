num=int(input('enter how many numbers you want to enter:'))
print('enter ',num,'numbers')
sum=0
for x in range(num):
    val=int(input())
    sum=sum+val

print('The average is',(sum/num))