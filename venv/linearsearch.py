num=int(input('enter no of values u want to enter'))
print('enter',num,'values')
list=list()
for x in range(num):
    val=input()
    list.append(val)

key=input('enter the value u want to search:')
boolean=False
for x in list:
    if(x==key):
        print('yes it is in list')
        boolean=True
if(boolean==False):
    print('no element found')