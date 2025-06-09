num = int(input("Enter a number: "))
for i in range(1, num + 1):
    print(i, oct(i)[2:], hex(i)[2:], bin(i)[2:])