#[2, 6, 8, 9]
date = "6/15/2023"

#get the month, day, and year values from date
#use the .split() strig method
date_parts = date.split("/")

#assign day, month, year to variables
month_number = int(date_parts[0])
day = date_parts[1]
year = date_parts[2]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#print day, month, year
print(f"Day: {day}")
print(f"Month: {months[month_number - 1]}")
print(f"Year: {year}")