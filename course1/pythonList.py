'''
# empty list
a_list = []
print("empty list:", a_list)

# integer list
a_int = [1, 2, 3, 4, 5]
print("integer list:", a_int)

# float list
a_float = [0.1, 0.2, 0.3, .4, .5]
print("float list:", a_float)

# string list
a_string = ['apple', 'banana', 'orange', 'grapes', 'mango']
print("string list:", a_string)

# mixed dataType list
a_mix = [1, 1.5, 'a', 'aniket']
print("mixed dataType list:", a_mix)

a_mix = [1, 1.5, 'a', 'jain']
print(a_mix[3])


nested_list = ['hello', [1, 2, 3]]
print(nested_list[1])
print(nested_list[1][2])  # output: 3
print(nested_list[1][0])  # output: 1
'''

a = [1, 2, 3, 4, 5]
print(a[-2])  # output: 4
print(a[-1])  # output: 5
print("length:", len(a))
