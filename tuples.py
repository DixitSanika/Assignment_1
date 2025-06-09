num = int(input("Enter a number: "))
nums = tuple(map(int, input("Enter the numbers: ").split()))
print("The hash of the tuple is: ",hash(nums))