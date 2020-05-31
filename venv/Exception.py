# we can handle the exceptions in python using try,except and finally blocks
try:
    print(x)
except NameError:
    print('variable x is not defined')
except:
    print('something went wrong')