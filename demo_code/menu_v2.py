
"""
Function to load menu items and cost into a dictionary
Input: none
Output: Dictionary of menu items and cost
"""
def get_menu_dictionary():
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

    #return dictionary
    return menu_item

def main():

    menu_items = get_menu_dictionary()
    
    total = 0
    while True:
        #prompt the user of a menu item
        item = input("Item: ")

        #determine if we need to end the program
        if item.lower() == "end":
            break
        elif item.title() not in menu_items.keys():
            continue

        #derermine the ordered item and add to total. If item not in dictionary then reprompt user
        total += menu_items[item.title()]

        #Display order total
        print(f"Total: ${total:.2f}")

    
main()

