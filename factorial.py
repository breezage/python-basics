# Find the factorial of a number provided by the user.

number = 5
#number = int(input("Enter a number: "))

factorial = 1

if number < 0:
   print("Error: cannot find factorial for negative numbers")
elif number == 0:
   print("Factorial of 0 is 1")
else:
   for i in range(1,number + 1):
       factorial = factorial*i
   print("The factorial of",number,"is",factorial)
