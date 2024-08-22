# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary. 
# Then, print the dictionary to the console.

info = {}
name = input('What is your name? ')
age = input('How old are you? ')
color = input('What is your favorite color? ')

info['Name'] = name
info['Age'] = age
info['Color'] = color

print(info)