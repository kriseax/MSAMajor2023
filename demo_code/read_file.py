#Reading files in python
#open the file
data_file = open("file.txt", "r")

#create an empty dictionary
menu_item = {}

#loop through data in the file
for line_of_data in data_file:
    #what do we need to do to each line of data?
    #split line of data at the ", "
    keys_values = line_of_data.split(", ")

    #create an entry to the dictionary. Remeber to convert price to float
    #key = keys_values[0]
    #value = float(keys_values[1])
    menu_item[keys_values[0]] = float(keys_values[1])

#close file
data_file.close()

for item, price in menu_item.items():
    print(f"{item}: ${price:.2f}")