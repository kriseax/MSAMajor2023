import requests
import time
from bs4 import BeautifulSoup

def export_data(list_of_stocks):
    export_file = open("stocks.csv", "w")

    #write a header row in the csv file
    header_row = ""
    for key in list_of_stocks[0]:
        header_row += key+","

    export_file.write(f"{header_row}\n")

    #loop through list of stocks
    for stock in list_of_stocks:
        stock_record = ""
        #write stock indicators to the file
        for indicator, value in stock.items():
            stock_record += value+","
        #write record to file
        export_file.write(f"{stock_record}\n")
    
    export_file.close()
    
    return

"""
Function to load stock data into a dictionary
Input: None
Output: dictionary of company symbols and names
"""
def load_company_dictionaries():
    company_dictionary = {}

    try:
        #open file
        stock_file = open("stock_list.csv")
        
        counter = 0
        for line_of_data in stock_file:
            counter += 1
            if counter == 1:
                continue
            
            stock_data = line_of_data.split(",", 1)
            company_dictionary[stock_data[0]] = stock_data[1].strip()
        stock_file.close()
    except:
        print("ERROR loading stock symbols.\n")
    
    return company_dictionary


def main():
    headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
    
    #symbols_list = ["GOOGL", "IBM", "SBUX", "AMC", "NFLX", "TSLA", "BA", "CSCO", "INTC", "ORCL", "JNJ", "WMT"]
    symbol_dictionary = load_company_dictionaries()
    list_of_stock_dictionaries = []
    
    for symbol in symbol_dictionary:
        print(f"Requesting stock data for {symbol_dictionary[symbol]}: {symbol}")
        url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'

        #request the page
        response = requests.get(url, headers=headers)

        #parse html and create a bueatiful soup object
        soup = BeautifulSoup(response.text, 'html.parser')

        stock_dictionary = {}
        stock_dictionary['symbol'] = symbol

        counter = 1
        #loop through the cell in the table
        for cell in soup.find_all('td'):
            #odd iterations are keys. Set key on odd numbered iterations
            if counter % 2 != 0:
                key = cell.text
            else:
                #enter key, value info in to the dictionary on even iterations
                value = cell.text.replace(",", "")
                stock_dictionary[key] = value
            #increment counter
            counter += 1
        
        #append stock dictionary to the list of dictionaries
        list_of_stock_dictionaries.append(stock_dictionary)

        #time.sleep(2)
    
    export_data(list_of_stock_dictionaries)

main()