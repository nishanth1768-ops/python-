# 1. Take your name as input and print it in uppercase.
name = input("Enter your name: ")
print(name.upper())

# 2. Take a sentence and convert it into lowercase.
sentence = input("Enter a sentence: ")
print(sentence.lower())

# 3. Enter a sentence and print it with the first letter capitalized.
sentence_cap = input("Enter a sentence: ")
print(sentence_cap.capitalize())

# 4. Use format() to display your name and age in a sentence.
my_name = "Alex"
my_age = 25
print("Hello, my name is {} and I am {} years old.".format(my_name, my_age))

# 5. Find the index of a given character in a word.
word = "Python"
print(word.index("t"))  # Throws ValueError if not found

# 6. Find the position of a substring in a sentence using find().
text = "Learning Python is fun."
print(text.find("Python"))  # Returns -1 if not found

# 7. Check if a word ends with "ing" using endswith().
check_word = "coding"
print(check_word.endswith("ing"))

# 8. Print a string with tabs (\t) and then use expandtabs() to show spaces.
tabbed_str = "Name\tAge\tCity"
print("Original:", tabbed_str)
print("Expanded:", tabbed_str.expandtabs(12))

# 9. Encode a string into UTF-8 using encode().
normal_str = "Hello World"
print(normal_str.encode(encoding="utf-8"))

# 10. Check if a string contains only digits using isdigit().
digit_str = "12345"
print(digit_str.isdigit())

# 11. Check if a string is numeric using isnumeric().
numeric_str = "½"
print(numeric_str.isnumeric())

# 12. Check if a string is alphanumeric using isalnum().
alnum_str = "Python3"
print(alnum_str.isalnum())

# 13. Check if a string contains only ASCII characters using isascii().
ascii_str = "Hello123!"
print(ascii_str.isascii())

# 14. Check if a string contains only alphabets using isalpha().
alpha_str = "Programming"
print(alpha_str.isalpha())
