#13. Write a function that calculates the area of a rectangle.
def area_react(l,b):
    return l*b 
l = int(input(" Enter the length of reactangle  "))
b = int(input( " Enter the breadth of reactangle "))
result = area_react(l,b) 
print(" area = " , result)