
#Create a list
demo_list = [15, 8, 64, 25, 9, 11, 32, 41]

#Matrix dimensions 3 x 4
list_of_lists = [[2, 4, 7, 9],
                 [3, 7, 8, 4],
                 [1, 8, 5, 2]]

#Get data from lists
print(demo_list[2])

#print the 8 in list_of_lists
print(list_of_lists[1][2])

#print all the values in my list_of_list matrix
for number in demo_list:
    print(number)

print("\n")
#iterate over the rows
for row in range(len(list_of_lists)):
    #iterate over the columns
    print(f"\nRow {row + 1} Values")
    for column in range(len(list_of_lists[row])):
        print(list_of_lists[row][column])
    
    



