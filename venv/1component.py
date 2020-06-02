def isbin(val):
    binval=str(val)
    #print(len(binval))
    count=0
    for x in binval:
        #print(x)
        if((x=='0' or x=='1')):
            count+=1
    #print(boolean)
    final = ''
    if (count==len(binval)):
        demo= str(val)
        for x in demo:
            if (x == '1'):
                final = final + '0'
            else:
                final += '1'

        print('1\'s component of the ', val, ' is ', final)
    else:
        print('Given number is not a binary number')

val=int(input('Enter a binary number'))
isbin(val)


