#1
i = 1
while i <= 10:
    print(i)
    i += 1
#2
i = 10
while i >= 1:
    print(i)
    i -= 1
#3
i = 2
while i <= 20:
    print(i)
    i += 2
#4
i = 1
while i <= 20:
    print(i)
    i += 2    
#5
N = 5# Change this value to test different numbers
total_sum = 0
i = 1
while i <= N:
    total_sum += i
    i += 1

print(total_sum)
#6
num = 7  # Change this value for a different table
i = 1

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
#7
num = 5  # Change this value to find a different factorial
factorial = 1
i = num

while i > 0:
    factorial *= i
    i -= 1

print(factorial)
#8
num = 12345
reversed_num = 0

while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10

print(reversed_num)
#9
num = 121
original = num
reversed_num = 0

while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10

if original == reversed_num:
    print("Palindrome number")
else:
    print("Not a palindrome number")
#10
num = 1124
digit_sum = 0
digit_product = 1

while num > 0:
    digit = num % 10
    digit_sum += digit
    digit_product *= digit
    num = num // 10

if digit_sum == digit_product:
    print("Spy number")
else:
    print("Not a spy number")


