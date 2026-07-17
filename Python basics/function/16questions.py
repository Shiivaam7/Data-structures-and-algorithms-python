#16. Write a function that converts Fahrenheit to Celsius 
def Fahrenheit_to_Celsius(fahrenheit):
    return (fahrenheit-32) *5/9 
temp = float(input("Enter the value of fahrenheit  ")) 
result = Fahrenheit_to_Celsius(temp)
print(result)
    