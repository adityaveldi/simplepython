# sorting the values which are given
num=int(input('enter the number of values u want to enter'))
list=list()
for x in range(1,num+1):
    print('Enter the ',x,' value')
    num=int(input())
    list.append(num)

list.sort()
print('After Sorting :')
print(list)
