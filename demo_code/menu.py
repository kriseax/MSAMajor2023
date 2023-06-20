
def main():

    menu_items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00}
    
    total = 0
    while True:
        #prompt the user of a menu item
        item = input("Item: ")

        #determine if we need to end the program
        if item.lower() == "end":
            break

        #derermine the ordered item and add to total. If item not in dictionary then reprompt user
        try:
            total += menu_items[item.title()]
        except:
            continue

        #Display order total
        print(f"Total: ${total:.2f}")

    
main()

