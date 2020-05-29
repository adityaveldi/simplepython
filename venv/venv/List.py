# list is the collection of objects which is changeable and allows duplication.
list_demo=[1,2,3,4,5]
print(type(list_demo))
ls=list_demo
# some inbuilt functions in list datatype.
# different types to access the list elements.
print(ls)
#sclicing
print(ls[2:5])
#negative indexing
print(ls[-4:-1])
# using loops
for x in ls:
    print(x)
# len gives the length of the list
print(len(ls))
"""" to add an element to the list we use append method . it adds at the end of the list only single value
 we can append"""
# we can use triple double quotes for multi-line comment
ls.append(6)
print(ls)
#to remove specific element
ls.remove(6)
print(ls)
# to reverse
ls.reverse()
print(ls)
# to sort default accending for decending make reverse=true as shown below
ls.sort()
print(ls)
ls.sort(reverse=True)
print(ls)
