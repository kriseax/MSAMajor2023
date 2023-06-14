#prompt the user to enter 2 numbers and output the sum of the two numbers
#Algorithm
#Inputs

#Function to prompt user for an integer input
#Function returns the integer
def get_positive_integer_input(prompt):
    while True:
        try:
            number1 = float(input(prompt))
            #determine if number <= 0
            if number1 <= 0:
                print("ERROR: Enter a value greater than 0.\n")
                #go back to the beginning of the loop
                continue
            break
        except ValueError:
            print("ERROR: please enter a valid number")

    return number1

def main():
    #1. ask the user for the first number and convert to an integer
    #if error occurs, reprompt the user to enter a correct value
    number1 = get_positive_integer_input("Enter the first value: ")
    number2 = get_positive_integer_input("Enter the second value: ")

    #Process data
    #3. Calculate the sum of the two numbers
    sum_of_numbers = number1 + number2

    #Output
    #4. print the answer to the user
    #"The answer to x + y = sum"
    print(f"The answer to {number1} + {number2} = {sum_of_numbers:.2f}")

main()
