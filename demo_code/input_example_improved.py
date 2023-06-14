#prompt the user to enter 2 numbers and output the sum of the two numbers

#Algorithm
#Inputs
#1. ask the user for the first number and convert to an integer
#if error occurs, reprompt the user to enter a correct value

while True:
    try:
        number1 = int(input("Enter the first value: "))
        break
    except ValueError:
        print("ERROR: please enter a valid number")

#2. ask the user for the second number and convert to an interger
while True:
    try:
        number2 = int(input("Enter the second value: "))
        break
    except ValueError:
        print("ERROR: please enter a valid number")

#Process data
#3. Calculate the sum of the two numbers
sum_of_numbers = number1 + number2

#Output
#4. print the answer to the user
#"The answer to x + y = sum"
print(f"The answer to {number1} + {number2} = {sum_of_numbers}")

