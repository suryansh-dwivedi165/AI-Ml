num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before swap: a = ", num1, "b = ", num2) 

# using third variable 
temp = num1
num1 = num2 
num2 = temp

print("After swap: a = ", num1, "b = ", num2) 