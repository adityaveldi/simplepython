value=input('enter the value:')
str=str(value)
val=str[-1::-1]
if(val==str):
    print('palindorme')
else:
    print('Not a palindorme')