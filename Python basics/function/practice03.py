# # 11. Convert the string '123' into an integer and add 10 to it.
# number = '123'
# number1 = int(number)
# result = number1 + 10
# print(result)

# 12. Convert the integer 50 into a float and a string. Print both
# number = 50

# # Convert to float
# number_float = float(number)

# # Convert to string
# number_str = str(number)

# print(number_float)      
# print(number_str)        
# print(type(number_float)) 
# print(type(number_str))    

# # 13. Take input as a string and convert it into an integer, then multiply by 2.
# user_input = input("enter the value")
# number = int(user_input)
# result = number*5
# print(result)

#14. Convert a boolean False into an integer.
# value = False
# number = int(value)
# print(number)



#15. Write a program to add two numbers given as strings after converting them into integers.
# num1 = input(str("enter the number: "))
# num2 = input(str("enter the number: "))

# int_num1 = int(num1)
# int_num2 = int(num2)

# print(int_num1+int_num2)

# 16. Take two numbers as input and calculate their average (with typecasting).
# num1 = input("enter the number: ")
# num2 = input("enter the number: ")

# num1 = float(num1)
# num2 = float(num2)
# result = num1+num2/2
# print(f" average is " , result)


# 17. Convert 123.45 to an integer and print the result.
# num1 = 123.45
# num2 = int(num1)
# print(num2)

#18. Demonstrate implicit and explicit typecasting with an example.
# num1 = 10.23
# num2 = 12
# print(num1+num2)
# print(type(num1+num2))#implict

# number = "45"
# x =int(number)#explicit
# print(x)
# print(type(x))

#19. Convert a list of numbers (as strings) into integers using a loop.
string_numbers = ["10", "20", "30", "40", "50"]  # list of numbers as strings
int_numbers = []  # empty list to store converted integers


for num in string_numbers:
    int_numbers.append(int(num))

print("Converted list:", int_numbers)

# 20. Convert an integer into binary and hexadecimal format using Python functions
num = 45  # You can change this number to anything

# Convert to binary
binary_format = bin(num)

# Convert to hexadecimal
hex_format = hex(num)

print("Original number:", num)
print("Binary format:", binary_format)
print("Hexadecimal format:", hex_format)
