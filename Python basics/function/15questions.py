#Write a function that converts Celsius to Fahrenheit. 
def celsius_to_fahrenheit(celsius):
    return (celsius *9/5) +32
temp = float(input("enter the celsius_value  "))
result = celsius_to_fahrenheit(temp)
print(result)