# append()
'''
fruit = ['apple', 'banana', "orange"]
print(fruit)
fruit.append("mango")
print(fruit)
'''

# extend()
'''
lang1 = ['java', 'python']
lang2 = ['c', 'c++']
print("Language 1:", lang1)
print("Language 2:", lang2)
lang2.extend(lang1)
print("Languages:", lang2)
'''

# index()
'''
lang = ['java', 'c', 'c++', 'python']
print(lang.index('c'))
'''

# insert()
'''
lang = ['java', 'c', 'c++']
print(lang)
lang.insert(0, 'python')
print(lang)
'''

# count()
'''
list = [1, 2, 3, 1, 2, 3, 1, 5]
print(list.count(1))
print(list.count(3))
'''

# remove()
'''
vowels = ['a', 'b', 'd', 'e', 'i', 'o', "u"]
print(vowels)
vowels.remove('b')
vowels.remove('d')
print(vowels)
'''

# pop()
'''
lang = ['java', 'c', 'c++', 'python']
print(lang)
lang.pop()  # by default from the right side of list
print(lang)
lang.pop(1)
print(lang)
'''
# reverse()
'''
chars = ['a', 'b', 'c', 'd', 'e']
print(chars)
chars.reverse()
print(chars)
'''

# sort
'''
int_list = [4, 1, 3, 5, 2, 3]
print("Un-ordered list:", int_list)
int_list.sort()  # ascending by default
print("Ascending order:", int_list)
int_list.sort(reverse=True)
print("Descending order:", int_list)

chars = ['a', 'c', 'b', 'e', 'd']
print(chars)
chars.sort(reverse=True)
print(chars)
'''
