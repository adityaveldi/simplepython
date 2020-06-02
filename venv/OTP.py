# generating a random number
import random
a=int(input('enter how many random number you want to generate: '))
for x in range(a):
    print(random.randint(1,1000))