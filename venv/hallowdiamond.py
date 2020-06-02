n=int(input('Enter the value:'))
for x in range(n+1):
    if(x==0 or x==n):
        for y in range(n):
            print('*',end=' ')

    else:
        for y in range(n):
            if(y==x or y==0 or y==n-1):
                print('*',end=' ')
            else:
                print(' ',end=' ')

    print(end='\n')