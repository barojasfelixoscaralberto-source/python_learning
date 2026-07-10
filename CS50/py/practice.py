first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

print("The three numbers are:", first, second, third)

if first > second and first > third:
    print("The largest number is:", first)
elif second > first and second > third:
    print("The largest number is:", second)
else:
    print("The largest number is:", third)

print("The sum of the three numbers is:", first + second + third)
