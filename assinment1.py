# assignment1.py
print("1 - add")
print("2 - subtract")
print("3 - multiply")
print("4 - divide")

# Get the user's choice
choice = int(input("Choose an option: "))

# Get the two numbers
first = float(input("First number: "))
second = float(input("Second number: "))

# Perform the chosen operation
if choice == 1:
    result = first + second
    print(f"{first} + {second} = {result}")

elif choice == 2:
    result = first - second
    print(f"{first} - {second} = {result}")

elif choice == 3:
    result = first * second
    print(f"{first} * {second} = {result}")

elif choice == 4:
    if second != 0:
        result = first / second
        print(f"{first} / {second} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid choice. Please run the program again.")
