# Math Interpreter Challenge

Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. You will write a program that enables users to do math, even without knowing Python.

In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

    x is an integer
    y is +, -, *, or /
    z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

## Requirements

- Prompt the user to enter a math expression in the format X y Z where y is a math operator (+, _, *, /)
  - "Expression: "
- Parse the expression to determine which operation to carry out and the value of the numbers
- Output the answer to the expression

## Sample Output

Expression: 1 + 1 
```
2.0 
```
Expression: 2 - 3 
```
-1.0
```
Expression: 2 * 2
```
4.0
```
Expression: 50 / 5 
```
10.0
```



