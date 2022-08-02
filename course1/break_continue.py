a = 'aniket'

print("break ex: ")
for x in a:
    if x == 'e':
        break
    print(x)

print("\ncontinue ex: ")
for x in a:
    if x == 'k' or x == "n":
        continue
    print(x)
