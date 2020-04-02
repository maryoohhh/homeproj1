# Building a user input

listtype = input("View original (o), sorted (s), reverse (r): ")

if listtype == 'o':
    print("Here is your original list")
elif listtype == 's':
    print("Here is your sorted list")
elif listtype == 'r':
    print("Here is your reverse sorted list")
else:
    print("Invalid choice")
