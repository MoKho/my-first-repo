number = int(input("Please enter a number to check:   "))
powerof = int(input("Please enter a power factor to check:   "))
while number % powerof == 0:
    number /= powerof
if number % powerof == 0 or number == 1:
    print("True")
else:
    print("False")

