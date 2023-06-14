
#For loop demo
#Print integers between 0 and 10
for x in range(11):
    print(x)

#print intergers between 5 and 10
print("\n\n")
for x in range(5, 11):
    print(x)

print("\n\n")
#print even number between 0 and 10
for x in range(0, 11, 2):
    print(x)

#prompt user for start and stop values
print("\n\n")
start_value = int(input("Enter start value: "))
stop_value = int(input("Enter end value: "))

for output in range(start_value, stop_value + 1):
    print(output)



