def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac*i
    print(fac)

num = int(input("Enter the number : "))
factorial(num)