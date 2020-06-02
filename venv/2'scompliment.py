def isbin(val):
    string=str(val)
    comp=''
    count=0
    for x in string:
        if(x=='0' or x=='1'):
            count+=1
    #print(boolean)
    if(count==len(string)):
        i=-1
        while(i>=(-len(string))):
           # print(string[i])
            comp = comp + string[i]
            if(string[i]=='1'):
                i-=1
                break
            else:
                i=i-1
       # comp=comp+string[i]
        while(i>=(-len(string))):
            if(string[i]=='1'):
                comp+='0'
                i-=1
            else:
                comp+='1'
                i-=1
        print('2\'s compliment of the given binary value is:',comp[-1::-1])
    else:
        print('Given number is not binary')


val=input('Enter the binary number:')
isbin(val)