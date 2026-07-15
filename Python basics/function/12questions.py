#12. Write a function that returns the smaller of two numbers.
def smaller_no(a,b):
    if a>b:
        return b 
    else:
        return a 
a = int(input( " Enter the first  number a  ")) 
b = int(input(" Enter the second number b  ")) 
result = smaller_no(a,b)
print(result)


