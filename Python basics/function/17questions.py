#7. Write a function that finds the length of a string. 
def len_of_string(string):
    count = 0
    for char in string:
        count += 1
    return count 
temp  = input("Enter the string = ") 
result = len_of_string(temp) 
print(result)
