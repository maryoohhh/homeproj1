# Building a user input

listtype = input("Please select what type of list you would like (o for original, s for sorted, r for reverse): ")

def type(i):
    switcher = {
        o: 'original'
        s: 'sorted'
        r: 'reverse'
    }
    return switcher.get(i, "Invalid choice")