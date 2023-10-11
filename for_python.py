names = ["a", "b", "c", "d", "e", "f"]

for name in names:
    print(name)


# for - else

# else will be executed
name = "asdfghjkl"
for i in name:
    print(i)
else:
    print("for loop executes completely")

# else will not be executed
name = "asdfghjkl"
for i in name:
    print(i)
    if i == "j":
        break
else:
    print("for loop executes only and only if fol loop executes completely")
