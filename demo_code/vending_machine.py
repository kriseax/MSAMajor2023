
def main():

    #assign amount due
    amount_due = 50

    while amount_due > 0:
        #Display the amount due
        print(f"Amount Due: {amount_due}")

        #Prompt the user to enter a coin
        coin = input("\nEnter Coin: ")

        #Validate coin amount and reprompt user if not valid value
        if coin not in ["1", "5", "10", "25"]:
            continue

        #convert coin to integer
        #coin = int(coin)

        #update amount due value amount_due = amount_due - coin
        amount_due -= int(coin)

    print(f"Change Owed: {amount_due * -1}")

main()

