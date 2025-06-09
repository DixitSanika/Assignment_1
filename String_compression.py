from itertools import groupby

a = input("Enter a string: ")
for letters, group in groupby(a):
    print(f"{letters},{len(list(group))}")
