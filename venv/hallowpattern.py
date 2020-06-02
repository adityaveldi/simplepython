n=int(input('Enter the number:'))
for x in range(n+1):
    if(x==0 or x==n):
        for y in range(n):
            print('*',end=' ')
    else:
        for y in range(n):
            if(y==0 or y==n-1):
                print('*',end=' ')
            else:
                print(' ',end=' ')

    print(end='\n')