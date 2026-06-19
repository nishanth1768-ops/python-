#List Tasks


# 1. Create a list of 5 student names and display it
students = ["Alice", "Charlie", "David", "Emma", "Charlie"]
print("Original list:", students)

# 2. Add a new element to the list using append()
students.append("Frank")
print("After append():", students)

# 3. Insert an element at the 2nd position (index 1)
students.insert(1, "Bob")
print("After insert at 2nd position:", students)

# 4. Remove an element from the list (removes first occurrence)
students.remove("David")
print("After removing David:", students)

# 5. Find the length of the list
print("Length of the list:", len(students))

# 6. Sort the list in ascending order
students.sort()
print("Sorted list:", students)

# 7. Reverse the list
students.reverse()
print("Reversed list:", students)

# 8. Find the largest number in a list (using numbers for this subtask)
numbers = [14, 52, 8, 91, 33]
print("Largest number in the list:", max(numbers))

# 9. Count the occurrence of an element
count_charlie = students.count("Charlie")
print("Occurrences of 'Charlie':", count_charlie)

# 10. Copy a list and display both lists
students_copy = students.copy()
print("Original List:", students)
print("Copied List:", students_copy)


#Tuple Tasks
# 1. Create a tuple of 5 numbers and display it
num_tuple = (10, 20, 30, 20, 40)
print("Original tuple:", num_tuple)

# 2. Find the length of a tuple
print("Length of tuple:", len(num_tuple))

# 3. Access the first and last elements of a tuple
print("First element:", num_tuple[0])
print("Last element:", num_tuple[-1])

# 4. Count how many times an element occurs in a tuple
print("Occurrences of 20:", num_tuple.count(20))

# 5. Find the index of a given element
print("Index of 30:", num_tuple.index(30))

# 6. Concatenate two tuples
another_tuple = (50, 60)
combined_tuple = num_tuple + another_tuple
print("Concatenated tuple:", combined_tuple)

# 7. Create a tuple containing different data types
mixed_tuple = ("Python", 3.14, True, 42)
print("Mixed data type tuple:", mixed_tuple)

# 8. Convert a list into a tuple
sample_list = [1, 2, 3]
converted_tuple = tuple(sample_list)
print("Converted to tuple:", converted_tuple)

# 9. Convert a tuple into a list
converted_list = list(num_tuple)
print("Converted to list:", converted_list)

# 10. Check whether a particular element exists in a tuple
element_exists = 30 in num_tuple
print("Does 30 exist in tuple?:", element_exists)

# Set Tasks

# 1. Create a set of 5 numbers and display it
num_set = {1, 2, 3, 4, 5}
print("Original set:", num_set)

# 2. Add a new element to the set
num_set.add(6)
print("After adding 6:", num_set)

# 3. Remove an element using remove() (Raises KeyError if element not found)
num_set.remove(2)
print("After remove(2):", num_set)

# 4. Remove an element using discard() (Does NOT raise an error if absent)
num_set.discard(10)  # 10 is not in the set, nothing happens
num_set.discard(3)   # 3 is removed
print("After discard statements:", num_set)

# Setup two sets for relationship tasks
set_A = {1, 4, 5, 6}
set_B = {5, 6, 7, 8}

# 5. Find the union of two sets
print("Union:", set_A.union(set_B))

# 6. Find the intersection of two sets
print("Intersection:", set_A.intersection(set_B))

# 7. Find the difference between two sets (Elements in A but not B)
print("Difference (set_A - set_B):", set_A.difference(set_B))

# 8. Check whether one set is a subset of another set
small_set = {5, 6}
print("Is small_set a subset of set_A?:", small_set.issubset(set_A))

# 9. Check whether one set is a superset of another set
print("Is set_A a superset of small_set?:", set_A.issuperset(small_set))

# 10. Clear all elements from a set
set_B.clear()
print("After clearing set_B:", set_B)


#Combined Tasks

# 1. Create a list, tuple, and set with the same elements and display them
base_elements = [10, 20, 30]
c_list = list(base_elements)
c_tuple = tuple(base_elements)
c_set = set(base_elements)
print("List:", c_list, "Tuple:", c_tuple, "Set:", c_set)

# 2. Convert a list into a tuple and a set
fresh_list = ["apple", "banana", "cherry"]
to_tuple = tuple(fresh_list)
to_set = set(fresh_list)

# 3. Convert a tuple into a list
fresh_tuple = ("x", "y", "z")
to_list = list(fresh_tuple)

# 4. Find common elements between two sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
common = s1.intersection(s2)
print("Common elements:", common)

# 5. Store student names in a list, tuple, and set
names = ["John", "Sophia", "Alex"]
student_list = list(names)
student_tuple = tuple(names)
student_set = set(names)

