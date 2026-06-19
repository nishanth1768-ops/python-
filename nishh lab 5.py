#Break Statement(for loop)

# 1. Print numbers from 1 to 20 and stop when the number is 10
for i in range(1, 21):
    if i == 10:
        break
    print(i, end=" ")
print()

# 2. Password checker that exits when the correct password is entered
correct_pwd = "secret123"
for _ in range(100):  # Arbitrary high range acting as a loop limit
    pwd = input("Enter password: ")
    if pwd == correct_pwd:
        print("Access Granted!")
        break

# 3. Accept numbers from the user and stop when the user enters 0
for _ in range(1000):
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    print(f"You entered: {num}")

# 4. Search for a specific element in a list and stop when it is found
items = ["apple", "banana", "cherry", "date"]
target = "cherry"
for item in items:
    if item == target:
        print(f"Found {target}!")
        break

# 5. Print numbers from 1 to 100 and stop at the first multiple of 17
for i in range(1, 101):
    if i % 17 == 0:
        print(f"First multiple of 17 is: {i}")
        break

# 6. Menu-driven program and exit when the user chooses "Exit"
menu_options = ["1. Start Game", "2. Settings", "3. Exit"]
for _ in range(100):
    print("\n".join(menu_options))
    choice = input("Choose an option: ")
    if choice == "3" or choice.lower() == "exit":
        print("Exiting...")
        break

# 7. Keep asking for input until the user enters "quit"
for _ in range(1000):
    user_input = input("Enter text (type 'quit' to exit): ")
    if user_input.lower() == "quit":
        break

# 8. Find the first even number in a list and stop the loop
numbers = [1, 3, 7, 8, 11, 14]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break

#Continue Statement - Task Questions


# 1. Print numbers from 1 to 20, skipping 10
for i in range(1, 21):
    if i == 10:
        continue
    print(i, end=" ")
print()

# 2. Print only odd numbers from 1 to 50
for i in range(1, 51):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# 3. Print only even numbers from 1 to 50
for i in range(1, 51):
    if i % 2 != 0:
        continue
    print(i, end=" ")
print()

# 4. Print numbers from 1 to 100, skipping multiples of 5
for i in range(1, 101):
    if i % 5 == 0:
        continue
    print(i, end=" ")
print()

# 5. Print all letters of a name except vowels
name = "Alice"
vowels = "aeiouAEIOU"
for letter in name:
    if letter in vowels:
        continue
    print(letter, end="")
print()

# 6. Print numbers from 1 to 30, skipping multiples of 3
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# 7. Print all elements in a list except negative numbers
mixed_list = [5, -3, 12, -1, 0, 8]
for num in mixed_list:
    if num < 0:
        continue
    print(num, end=" ")
print()

# 8. Print numbers from 1 to 20, skipping even numbers
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

#Pass Statement - Task Questions

# 1. Create an empty function called student_details()
def student_details():
    pass

# 2. Create an empty class called Employee
class Employee:
    pass

# 3. Write a while loop with a pass statement
condition = False
while condition:
    pass

# 4. Write a for loop with a pass statement
for i in range(5):
    pass

# 5. Create a placeholder function for a future calculator project
def future_calculator():
    pass

# 6. Create a placeholder class called BankAccount
class BankAccount:
    pass

# 7. Create a menu structure using pass for options not yet implemented
choice = "2"
if choice == "1":
    print("Starting...")
elif choice == "2":
    pass  # Feature coming soon
elif choice == "3":
    print("Exiting...")

# 8. Create an empty if block using pass
x = 10
if x > 5:
    pass


#Mixed Task Questions (Break, Continue, Pass)

# 1. Print numbers from 1 to 50: Skip multiples of 4, stop when the number reaches 40
for i in range(1, 51):
    if i == 40:
        break
    if i % 4 == 0:
        continue
    print(i, end=" ")
print()

# 2. Create a login system: Allow 3 attempts, exit using break when successful
correct_username = "admin"
correct_password = "password"
for attempt in range(1, 4):
    u = input("Username: ")
    p = input("Password: ")
    if u == correct_username and p == correct_password:
        print("Login Successful!")
        break
else:
    print("Account locked. Too many failed attempts.")

# 3. Print numbers from 1 to 100: Skip multiples of 10, stop at 75
for i in range(1, 101):
    if i == 75:
        break
    if i % 10 == 0:
        continue
    print(i, end=" ")
print()

# 4. Create a simple ATM menu: Use pass for unimplemented options, break to exit
for _ in range(100):
    print("1. Check Balance\n2. Withdraw\n3. Exit")
    action = input("Select: ")
    if action == "1":
        pass  # TODO: Balance logic
    elif action == "2":
        pass  # TODO: Withdrawal logic
    elif action == "3":
        print("Goodbye!")
        break

# 5. Print all numbers from 1 to 30: Skip even numbers, stop at 25
for i in range(1, 31):
    if i == 25:
        break
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

#While loop
#Break
# 1. Print numbers from 1 to 10 and stop at 5
i = 1
while i <= 10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1
print()

# 2. Print numbers from 1 to 20 and stop at 15
i = 1
while i <= 20:
    if i == 15:
        break
    print(i, end=" ")
    i += 1
print()

# 3. Keep asking for a number and stop when the user enters 0
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break

# 4. Keep asking for a password and stop when it is correct
saved_pwd = "pass"
while True:
    guess = input("Enter Password: ")
    if guess == saved_pwd:
        print("Correct!")
        break

# 5. Print numbers from 1 to 100 and stop at 50
i = 1
while i <= 100:
    if i == 50:
        break
    print(i, end=" ")
    i += 1
print()



#Continue
# 1. Print numbers from 1 to 10, skipping 5
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i, end=" ")
print()

# 2. Print numbers from 1 to 20, skipping 10
i = 0
while i < 20:
    i += 1
    if i == 10:
        continue
    print(i, end=" ")
print()

# 3. Print only odd numbers from 1 to 20
i = 0
while i < 20:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# 4. Print only even numbers from 1 to 20
i = 0
while i < 20:
    i += 1
    if i % 2 != 0:
        continue
    print(i, end=" ")
print()

# 5. Print numbers from 1 to 30, skipping multiples of 3
i = 0
while i < 30:
    i += 1
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()


#Pass
# 1. Print numbers from 1 to 20, skip 5, and stop at 15
i = 0
while i < 20:
    i += 1
    if i == 15:
        break
    if i == 5:
        continue
    print(i, end=" ")
print()

# 2. Print numbers from 1 to 30, skip multiples of 4, and stop at 25
i = 0
while i < 30:
    i += 1
    if i == 25:
        break
    if i % 4 == 0:
        continue
    print(i, end=" ")
print()

# 3. Login system with a while loop (break on success, continue skips code to ask again)
attempts = 0
while attempts < 3:
    user = input("User: ")
    pwd = input("Pass: ")
    if user == "user1" and pwd == "secure":
        print("Logged in!")
        break
    attempts += 1
    print(f"Wrong credentials. Attempts remaining: {3 - attempts}")
    continue

# 4. Print only odd numbers using continue (example from 1 to 10)
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# 5. Menu program with pass for unfinished options and break to exit
while True:
    print("\n--- Menu ---")
    print("1. Update Profile (Unfinished)")
    print("2. Log Out")
    option = input("Select option: ")
    
    if option == "1":
        pass
    elif option == "2":
        print("Logged out successfully.")
        break
