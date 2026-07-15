#14. Write a function that calculates the perimeter of a rectangle
def perimeter_of_reactangle(l,b):
    return 2*(l+b) 
l = int(input(" Enter the length value  "))
b = int(input(" Enter the breadth value  "))
result = perimeter_of_reactangle(l,b)
print("perimeter = ",result)