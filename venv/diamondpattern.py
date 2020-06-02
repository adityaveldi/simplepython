n=int(input('enter the value:'))
for i in range(n):
    count=0
    for x in range(i,n):
        print(' ',end=' ')
    #print(x,end='\n')
    for x in range(i+1):
        print('*',end=' ')
        count+=1
    if(count>1):
        for x in range(count,1,-1):
            print('*',end=' ')
    print(end='\n')

for i in range(n,-1,-1):
    count=0
    for x in range(i,n):
        print(' ',end=' ')
    #print(x,end='\n')
    for x in range(i+1):
        print('*',end=' ')
        count+=1
    for x in range(count,1,-1):
        print('*',end=' ')
    print(end='\n')

