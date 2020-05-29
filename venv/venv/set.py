# let us see about the sets
# set is the data type of which is the unodered collections and unindexed
# doesn't allow duplicates.
set={1,2,3,4,5}
print(set)
print(type(set))
# using for loop to display elements
for x in set:
    print(x)

#using add() we can add only single element ,by using update() we can add mutiple elements.
set.add(6)
print(set)
set.update([7,8,9])
print(set)
# to display length we use len()
print(len(set))
# to remove the elements use remove()
set.remove(5)
print(set)
# we can do set operations like union,intersection
set2={2,5,8,10}
set=set.union(set2)
print(set)
set=set.intersection(set2)
print(set)
#some more functions we can implement