liste = ["1", "4", "25", "Paul", "3", "Pierre"]
for i in liste:
    if i.isdigit():
        continue
    print(i)

liste = ["1", "4", "25", "Paul", "3", "Pierre"]
for i in liste:
    if i.isdigit():
        break
    print(i)
    