
def main():
    # Prompt the user for the expression
    expression = input("Expression: ")

    # Use .split() to get the parts of the expression. Split at the space
    expression_list = expression.split(" ")

    # Get values from list
    x = int(expression_list[0])
    operator = expression_list[1]
    z = int(expression_list[2])

    # Determine the type of operation to carry out. Using if/elif/else statement
    if operator == "+":
        answer = x + z
    elif operator == "-":
        answer = x - z
    elif operator == "*":
        answer = x * z
    else:
        answer = x / z
    # run the expression and print output formatted t one decimal place

    print(f"{answer:.1f}")

main()