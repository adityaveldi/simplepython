# tuple is the collection where the elements are ordered and unchangeable
tuple=(1,2,3,4,5)
print(tuple)
print(type(tuple))
for x in tuple:
    print(x)
# we can add two tuples just it concatinates
tuple=tuple+tuple
print(tuple)
# we can know the length using len()
print(len(tuple))
# count gives the number times given
print(tuple.count(2))
# we can use index() find the index of the given element first occurence.
print(tuple.index(2))
