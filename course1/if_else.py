# a = int(input("Enter the a: "))
# b = int(input("Enter the b: "))
# c = int(input("Enter the c: "))

a, b, c = int(input("Enter a: ")), int(
    input("Enter b: ")), int(input("Enter c: "))
if a == b == c:
    print("all values are equal.")
elif a > b and a > c:
    print("a is greater than b, c.")
elif b > c:
    print("b is greater than a, c.")
else:
    print("c is greater than a, b.")
print("End")
