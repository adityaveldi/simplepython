#dictionary is the collection of objects in the form of key value pairs
#keys must be unique and values can be duplicated
dict={'name':'Aditya','mno':2277681,'age':20}
print(type(dict))
print(dict)
# to get the value of specific ket we use get()
value=dict.get('name')
print(value)
# we can change the values of the keys as shown below
dict['mno']=6633214
print(dict)
# to get the key values
print('keys of the dict are:')
for x in dict:
    print(x)
# to get the values of the keys
print('values of the keys are')
for x in dict:
    print(dict[x])
# we can also access keys by using values()
print('values of the keys are displayed using values()')
for x in dict.values():
    print(x)
# to know the length of the dictionary use len() it shows no of elements ie no of key-value pairs
print('length is:')
print(len(dict))
# to copy to another dictonary
print('copying dictionary using copy()')
mydict=dict.copy()
print(mydict)