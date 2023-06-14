#While loop demo
#Print integers between 0 and 10

stop_value = 10
output_value = 0

while output_value <= stop_value:
    print(output_value)
    output_value = output_value + 1


print("\n\n")
output_value = 0
while True:
    print(output_value)
    output_value = output_value + 1

    #if output value > stop value. Exit the loop
    if output_value > stop_value:
        break

