#1
add = lambda x, y: x + y
print(add(20,30))

square = lambda x: x ** 2
print(square(23))

cube = lambda x: x ** 3
print(cube(33))

even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_odd(69))

largest = lambda x, y: x if x > y else y
print(largest(25,65))

#2
'''numbers=[2,5,9,8,7,6,3,28,42,-2]
evens=list(filter(lambda x:x%2 == 0,numbers))
print(evens)

odds=list(filter(lambda x:x%2 != 0,numbers))
print(odds)

greater_than_10=list(filter(lambda x:x>10,numbers))
print(greater_than_10)

positive_numbers=list(filter(lambda x:x>0,numbers))
print(positive_numbers)

numbers_divisible_by_5=list(filter(lambda x:x%5 == 0,numbers))
print(numbers_divisible_by_5))'''

#3
'''numbers=[5,6,3,8,2,1,4,7,6,9,25,4,51,56,25,5,15]
squares=list(map(lambda x:x ** 2,numbers))
print(squares)

doubles=list(map(lambda x:x*2,numbers))
print(doubles)

add_5=list(map(lambda x:x+5,numbers))
print(add_5)

cubes=list(map(lambda x:x ** 3,numbers))
print(cubes)

string=list(map(lambda x:str(x),numbers))
print(string)'''

#4
numbers=[1,2,3,4,5,-6]
even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(even_squares)


odd_doubled = list(map(lambda x: x * 2, filter(lambda x: x % 2 != 0, numbers)))
print(odd_doubled)

gt_5_cubes = list(map(lambda x: x ** 3, filter(lambda x: x > 5, numbers)))
print(gt_5_cubes)




                  
                  


































