x = int(input("Enter a number: "))
y = int(input("Enter another number: "))


# As an advice: when using conditionals and using only ifs, the code evaluates all the conditions
# However if instead you use elif as a secondary conditional, it'll only evaluate the first condition that is true and skip the rest. This is more efficient in some cases.
if x > y:
    print(f"{x} is greater than {y}")
if x < y:
    print(f"{x} is less than {y}")
if x == y:
    print(f"{x} is equal to {y}")
if (x + y) < 10:
    print("hi")