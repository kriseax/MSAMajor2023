#ask the user if they want to continue. If y, continue. If n end
#Incorrect operator format
#X or Z are not numbers
#Expression not in correct format. Has more than 3 parts

"""
Function to get valid expression inputs from user
Inputs: None
Outputs: (int)number1, (int)number2, (string)operator
"""
def get_valid_expression_inputs():
    while True:
        # Prompt the user for the expression
        expression = input("Expression: ")

        # Use .split() to get the parts of the expression. Split at the space
        expression_list = expression.split(" ")

        #Test for incorrect number of parts
        if len(expression_list) != 3:
            print("ERROR: Enter Expression in (X Y Z)format\n")
            continue

        # Get values from list
        try:
            x = int(expression_list[0])
            z = int(expression_list[2])
        except ValueError:
            print("ERROR: X and Z must be numbers. (X Y Z)\n")
            continue

        operator = expression_list[1]
        #test for correct operator (*, /, +, -)
        if operator not in ["+", "-", "*", "/"]:
            print("ERROR: Incorret operator. Only (+, -, *, /) allowed.\n")
            continue

        break
    
    return x, z, operator  

"""
Function to evaluate expression
Inputs: (int)x, (int)z, (string)operator
Output: (int)answer
"""
def evaluate_expression(number1, number2, symbol):
    # Determine the type of operation to carry out. Using if/elif/else statement
    if symbol == "+":
        answer = number1 + number2
    elif symbol == "-":
        answer = number1 - number2
    elif symbol == "*":
        answer = number1 * number2
    else:
        answer = number1 / number2
    
    return answer

def main():
    while True:

        #call get_valid_expression_inputs function to get the x, x, and operatorer values
        x, z, operator = get_valid_expression_inputs()

        # Call evaluate_expression to get the answer for the expression
        answer = evaluate_expression(x, z, operator)
        
        # run the expression and print output formatted to one decimal place
        print(f"{answer:.1f}")

        #Ask user if the want to continue
        another_calculation = input("Would you like to eavluate another expression? Press y to continue or any other key to exit: ").lower()
        
        #Determin the value of another_claculation and if we should break or not
        if another_calculation != "y":
            break


main()