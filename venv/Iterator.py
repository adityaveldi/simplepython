# every collection has iterator constructor that used to iterate through the collection object
list=[1,2,3,4,5]
mylist=iter(list)
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))

# we can also use the for loop as the iterator
print('using the for loop as the iterator')
for x in list:
    print(x)