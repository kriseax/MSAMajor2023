# Do you need to...'

You can think of your programming skills and knowledge as tools in a toolbox. You'll choose to use a particular tool depending on the task. This document is created to help you with choosing the correct tool.

- [Store a Value](#store-a-value)
- [Get user Input](#get-input-from-the-user)
- [Make a Decision](#have-your-code-make-a-decision)
- [For Loop](#the-for-loop). Run the Same Code Multiple Times 
- [While Loop](#the-while-loop). Run the Same Code Multiple Times 
- [Lists](#lists). Store multiple values in one structure.
- [Dictionaries](#dictionaries). Store associated data together

## Store a value

If you need to store a value create a variable. Remember that a variable is a named locaton in memory and storing that value in a variable will allow you to use it in other places in your program. Here is how you declare a variable:

```python
#This is a comment in Python
my_string = "Truman Tiger"
my_int = 5
my_float = 7.5
my_boolean = True 
```

You can choose any name for your variables but make sure they are meaningful and convey what the variable is being used for.

## Get input from the user

Use the ```input()``` function to get input from a user. You should store the user input in a variable

```python

user_input = input('Enter your name:')
print('Hello, ' + user_input) 
```

## Have your code make a decision

Decision making is required when we want to execute some code only if a certain condition is satisfied. The ```if…elif…else``` statement is used in Python for decision making.

### Python if statement

```python
# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")
```

### Python if...else Statement

```python
# Program checks if the number is positive or negative
# And displays an appropriate message

num = 3

# Try these two variations as well. 
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")
```

### Python if...elif...else Statement

```python
#In this program, we check if the number is positive or 
#negative or zero and display an appropriate message

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
```

## Run the same code multiple times? Use a Loop then

There are two kinds of loops: a ```for``` loop and a ```while``` loop. The ```for loop``` is a counter-based loop and you will use it if you know beforehand how many times you want the loop to run. The ```while loop``` is a condition-based loop that will continue to execute while a provided condition is true

### The For Loop

The for loop in Python is used to iterate, or loop, over a sequence (list, dictionary, string, tuple) or other iterable objects. Iterating over a sequence is called traversal.

```python
# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)
```

When you run the program, the output will be:

> The sum is 48

### The For Loop with range() function

We can generate a sequence of numbers using ```range()``` function. range(10) will generate numbers from 0 to 9 (10 numbers).

We can also define the start, stop and step size as range(start, stop,step_size). step_size defaults to 1 if not provided.

We can use the ```range()``` function in for loops to iterate through a sequence of numbers. It can be combined with the ```len()``` function to iterate through a sequence using indexing. Here is an example.

```python
# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])
```

### The While Loop

The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true. In the while loop, test expression is checked first.

> while test_expression:
    Body of while

The body of the loop is entered only if the ```test_expression``` evaluates to ```True```. After one iteration, the test expression is checked again. This process continues until the ```test_expression``` evaluates to ```False```.

```python
# Program to add natural numbers up to 
# sum = 1+2+3+...+n

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
```

## Store multiple values in one structure? Create a list

Lists are used to store multiple items in a single variable. Lists are created using square brackets[]

### Lists

```python
this_list = ["apple", "banana", "cherry"]
print(this_list)

#print the second item in the list. Code will print "banana"
print(this_list[1])
```

List items are indexed, the first item has index [0], the second item has index [1] etc. List values are ordered, changeable, and duplicates are allowed. 

You can add an item to a list usinf the ```append()``` method

```python
this_list = ["apple", "banana", "cherry"]
print(this_list)

#append two more items
this_list.append("grapes")
this_list.append("watermelon")
print(this_list)

```

The second print statement will print:

> ["apple", "banana", "cherry", "grapes", "watermelon"]

## Use Dictionaries to store associated data in key, value pairs

### Dictionaries

In Python, a dictionary is a built-in data structure that allows you to store and retrieve data in an unordered manner. It is also known as an associative array, hash map, or simply a map. Dictionaries in python are defined using curly braces {}, and they consist of key-value pairs. The keys in a dictionary must be unique. The keys are also immutable, meaning they canno change, and can be strings or numbers, while the corresponding values can be of any data type. Dictionaries provide an efficient way to store and access data, as the retrieval of values is based on the unique keys rather than the position of elements.

Here are three code examples demonstrating the usage of dictionaries in Python:

1. Creating a dictionary and accessing values:
```python
student = {'name': 'John Doe', 'age': 20, 'grade': 'A'}
print(student['name'])  # Output: John Doe
print(student['age'])   # Output: 20
print(student['grade']) # Output: A
```

In this example, a dictionary called student is created with keys 'name', 'age', and 'grade', along with their respective values. The values can be accessed using square brackets and the corresponding key.

2. Adding and modifying dictionary entries:
```python
student = {'name': 'John Doe', 'age': 20, 'grade': 'A'}
for key in student:
    print(key)          # Output: name, age, grade
    print(student[key]) # Output: John Doe, 20, A

```
In this example, the value corresponding to the 'age' key is modified from 20 to 21. Additionally, a new key-value pair 'score': 95 is added to the dictionary using assignment with a new key.

3. Iterating over dictionary keys to get the associated values values:
```python
student = {'name': 'John Doe', 'age': 20, 'grade': 'A'}
for key in student:
    print(key)          # Output: name, age, grade
    print(student[key]) # Output: John Doe, 20, A
```

In this example, a for loop is used to iterate over the keys of the student dictionary. Within the loop, both the keys and their corresponding values are accessed using the key in square brackets.

4. Iterating over dictionary keys and values in the loop header:
```python
student_grades = {'John': 85, 'Emily': 92, 'Michael': 78, 'Sophia': 95}

for name, grade in student_grades.items():
    print(f"{name} scored {grade} marks.")

# Output:
# John scored 85 marks.
# Emily scored 92 marks.
# Michael scored 78 marks.
# Sophia scored 95 marks.

```
In this example, we have a dictionary called student_grades, where the keys represent the names of the students and the values represent their respective grades. We iterate over the dictionary using the items() method, which returns each key-value pair as a tuple. The name and grade variables in the loop header represent the key and value of each iteration, respectively. We then use these variables to print out the name and corresponding grade for each student in a formatted string.

Dictionaries provide a powerful way to organize and manipulate data in Python, making them a valuable tool for various programming tasks.
