 #Write a function that returns the greater of two numbers 
def greater_no(a,b):
     if a>b:
         return a
     else: 
         return b
    
a = int(input("enter the first number "))
b = int(input("enter the second number "))

result = greater_no(a,b)
print(result)