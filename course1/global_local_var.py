from threading import local


def hello():
    global x
    x = 'hello'  # global variable
    y = 'world'  # local variable
    print(x, y)


hello()  # output: hello world

print()
print()
a = 'hello world'  # global variable
print(a, x)  # output: hello world hello
