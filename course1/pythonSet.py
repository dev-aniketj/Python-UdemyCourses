# SET doesn't allow duplicates
# set doesn't on support indexing,
# bcoz set is in un-order form
'''
set = {1, 7, 2, 3, 3, 6, 5, 4, 1, 2}
print(set)

set = {1, 1.0, 1.3, 'hello world'}
print(set)
set.add(2)  # add single items/element
print(set)
set.update([4, 5, 6])  # add multiple items/elements
print(set)
set.remove('hello world')  # remove single item/element
print(set)
'''

# Set Operation - union & intersection
# Union - set of all elements in both
# Intersection - common elements in both
a = {0, 1, 2, 3, 5}
b = {3, 4, 5, 6}
print("Union:", a | b)
print("Intersection:", a & b)
