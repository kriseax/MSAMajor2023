# Scenario

You and a number of IT students are going to a ski trip/hackathon over winter break in Colorado. To manage sign ups, the program has asked your team to create a simple web based reservation system so that students can reserve their seats on the bus. Students will be charged different amounts based on the seat they pick. You will be provided with a pricing chart for the seating.

## Requirements

Create a menu-driven reservation system using Flask Python, or another language with the ability to load and save reservations data to/from a file. The application should also allow an administrator to login to the admin portal where they can view the bus seating chart and see the total sales. The bus can seat up to 48 people, 12 rows of 4 seats each. You can use your project 3a as a template for this project.

Your application will need to have the following functionality:

    A. Create a seating chart and load the initial reservations
    B. Display the main menu that asks the user whether they want to reserve a seat or log in as an administrator
    C. If the user selects the admin login option they are taken to a page with a form to login. Information the user provides:
        admin username
        admin password
    D. If the user successfully logs in a seating chart is displayed along with the total sales collected.
    E. If the user selects the the reservation option they are taken to a page with a form to reserve a seat. Information the user provides
        first name
        last name
        seat row
        seat column
    F. Display a flight chart
    G. Calculate and get the total sales for the flight when the user successfully logs in as an admin
    H. Create and print a reservation code for the user when the user successfully makes a reservation
    I. Save the reservation in formation the reservation.txt (first name, seat row, seat column, e_ticket number)
    J. Each page should have a link to the main option page.

Cost Matrix: You will need pricing a matrix to calculate sales for the flight. The following python function will create a 12 x 4 cost matrix which represents the cost of each seat on the flight. You should use this code in your project.

```
'''
Function to generate cost matrix for flights
Input: none
Output: Returns a 12 x 4 matrix of prices
'''
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix
```

## Video Demo
[Video Link](https://umsystem.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b2777155-fdf0-4a8f-8708-afee001c1cf1)
