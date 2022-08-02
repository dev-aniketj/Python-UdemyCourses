# int + int  = int
# int + float = float
# float + float = float
# float + int = float
# str + int = error
# str + float = error


# Implicit type conversion

'''
python automatically convert one to another
'''

a = 10  # int
b = 10.57  # float
c = a + b  # float
print(type(a))
print(type(b))
print(type(c))
print(a)
print(b)
print(c)

print()

# explicit type conversion
'''
user convert dataType
'''
a = 10  # int
b = "20"  # str (String)
print(type(a))
print(type(b))
# c = int(b)  # int - type conversion
# d = a + c  # int output: 30
c = a + int(b)
print(c)
print(type(c))
