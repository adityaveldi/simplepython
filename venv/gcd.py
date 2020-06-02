def gcd(m,n):
    min=m
    if(min>n):
        min=n
    for x in range(min,0,-1):
        if(m%x==0 and n%x==0):
            return x
        else:
            continue


v1=int(input('Enter first number:'))
v2=int(input('Enter second number:'))
value=gcd(v1,v2)
print('GCD is:',value)