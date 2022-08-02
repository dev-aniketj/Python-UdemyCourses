# Python Tuple

# simple tuple
'''
e_tuple = (1, 2, 3, 4, 5)
print(e_tuple[0])
print(e_tuple[2])
print(e_tuple[4])
'''

# nested tuple
'''
nested_tuple = ('hello', 'world', ('aniket', "jain"))
print(nested_tuple[2][1])
print(nested_tuple[1])
print(nested_tuple[2])
'''

# negative index
'''
tuple = (1, 2, 3, 4, 5)
print(tuple[-1])
print(tuple[-3])
'''

# add tuple

# x = (1, 2, 3) + ('a', 'b', 'c')
# print(x)

x = (1, 2, 3)
y = ('a', 'b', 'c')
z = x + y
print(z)
