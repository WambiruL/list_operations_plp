# Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.

set_one = set()
set_two = set()

user_input1 = input("Enter 3 Integers, separated by commas: ")
set_one= set(map(int, user_input1.split(',')))
user_input2 = input("Enter other 3 Integers, separated by a comma: ")
set_two= set(map(int, user_input2.split(',')))
print(set_one)
print(set_two)

print("Common elements:", set_one & set_two)