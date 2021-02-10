import sys
import pandas as pd
from alpha_vantage.timeseries import TimeSeries # Alpha_vantage_wrapper

# replace this API key with your own in case you obtained your own

API_KEY = 'RDRQUL64Q2ZAT7L4'

def getStockdata(symbol):

    try:

        print("Gathering info....")

        timeSeries = TimeSeries(key=API_KEY, output_format='pandas')

        data, meta_data = timeSeries.get_intraday(symbol=symbol, interval='1min')

        return str(data.tail(1).iloc[0]['4. close'])

    except:

        return "not found"

def main():

    outFile = open('japi.py', 'w')

    while 1:

        userInput = input("Enter Stock Symbol or EXIT to exit: ").upper()

        if userInput != "EXIT":

            serverData = 'The current price of {} is {}\n'.format(userInput, getStockdata(userInput))

            print(serverData)

            outFile.write(serverData)

        else:

            sys.exit("\nThank you for using the program!\n")



main()
print("Stock Quotes retrieved successfully!")