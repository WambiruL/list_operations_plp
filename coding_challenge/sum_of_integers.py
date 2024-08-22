# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

total_sum = 0
while True:
    number = int(input("Enter integers to find the sum: "))
    
    total_sum +=number
    print(total_sum)


