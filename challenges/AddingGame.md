# Adding Game Challenge
Create a program in python called adding_game.py that prompts a user to answer a series of addition problems. The program will keep track of the number of correct and incorrect answers and display the result at the end.

## Requirements

Your program should meet the following requirements:

- The program should prompt the user for a difficulty level. Valid options are 1, 2, or 3.If the user does not input 1, 2, or 3, the program should prompt again.
- The program should prompt the user for the number of questions to ask. Valid options are  1 - 10.If the user does not input 1 - 10, the program should prompt again.
- The program should randomly generate the number of questions the user entered in the previous step. For example, if the user entered 5 for the number of questions the program should ask, the program should then generate 5 math problems. Likewise, if they entered 10 the program should generate 10 problems. The problems should be formatted as X + Y = , wherein each of X and Y is a non-negative integer with difficulty level of digits. For example:
  - If the user chose difficulty level 1 then X and Y should be 1 digit, non-negative, numbers (0 - 9).
  - If the user chose difficulty level 2 then X and Y should be 2 digit, non-negative, numbers (10 - 99).
  - If the user chose difficulty level 3 then X and Y should be 3 digit, non-negative, numbers (100 - 999).
- Your program does not need to support operations other than addition (+).
- The program should prompt the user to solve each problem.
  - If an answer is correct the program should output CORRECT!!! and the prompt the user to answer the next question.
  - If an answer is not correct (or not even a number), the program should output WRONG!!! and prompt the user again, allowing the user up to three tries in total to answer the question. If the user has still not answered correctly after three tries, the program should output the correct answer and the prompt the user to answer the next question.
- The program should ultimately output the user’s score and the percentage (formatted to 2 decimal places) correct.
- End the program

## Sample Output

```
Enter Level 1, 2, 3: 5
Error: Invalid input!

Enter Level 1, 2, 3: ff
Error: Invalid input!

Enter Level 1, 2, 3: 1

Enter number of questions to ask: 3 to 10: 12
ERROR: Please enter an integer value between 3 and 10!

Enter number of questions to ask: 3 to 10: 3

2 + 2 = 4
CORRECT!!!

2 + 3 = 6
WRONG!!!

2 + 3 = 7
WRONG!!!

2 + 3 = 8
WRONG!!!

Correct Answer: 2 + 3 = 5

7 + 5 = 11
WRONG!!!

7 + 5 = 12
CORRECT!!!


You got 2 out of 3 questions correct: 66.67%
```
