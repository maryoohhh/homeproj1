# Building a user input

listtype = input("View original (o), sorted (s), reverse (r): ")

def lst(i):
    switcher = {
        o: 'original list',
        s: 'sorted list',
        r: 'reverse list'
    }
    return switcher.get(i, "Invalid choice")

print("Here is the ", end="")
print(lst, end=".")