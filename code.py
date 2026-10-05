# Import all the modules needed for this web scraping project

from bs4 import BeautifulSoup
import requests

from datetime import datetime

import pandas as pd

import os

import time


# Create a function and put all the code for web scraping in this function

def automated_crypto_pull():
    # Create a variable for the link to the crypto website from which we want to scrape data
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    # Make a request to the crypto webstie and assign it to a variable
    page = requests.get(url)
    # Pull in the html
    soup = BeautifulSoup(page.text, 'html')

    # Use the title attribute to get what the name of the crypto of choice, Bitcoin, and save it to a variable
    crypto_name = soup.find('span', title = 'Bitcoin')['title']

    # Use the class attribute below to get the price of Bitcoin, get rid of the dollar sign, and assign it to a variable
    crypto_price = soup.find('span', 'sc-c1554bc0-0 RbQXx base-text').text.replace('$', '')

    # Get the timespan and assign it to a variable
    date_time = datetime.now()

    # Create a dictionary that contains the name of the cryptocurreny, the price, and the timestamp
    dict = {'Crypto Name': crypto_name, 
            'Price': crypto_price,
            'TimeStamp': date_time}

    # Put the dictionary into a list, put it into a data frame, and assign the data frame to a variable
    # We need to put the dictionary into a list first, or Python will return an error message: "ValueError: If using all scalar values, you must pass an index"
    df = pd.DataFrame([dict])

    # Write an if statement to append new data to the csv file if it already exists, and if it doesn't already exist, create a new csv file
    # mode = 'a' stands for append
    # header = False means don't include header
    # index = False means don't include index
    if os.path.exists(r'/Users/bronnie0826/Documents/Analyst_Builder/Python_Programming_for_Beginners/16_Project 4 - Automated Crypto Web Scraper/Bitcoin_Price.csv'):
        df.to_csv(r'/Users/bronnie0826/Documents/Analyst_Builder/Python_Programming_for_Beginners/16_Project 4 - Automated Crypto Web Scraper/Bitcoin_Price.csv', mode = 'a', header = False, index = False)
    else:
        df.to_csv(r'/Users/bronnie0826/Documents/Analyst_Builder/Python_Programming_for_Beginners/16_Project 4 - Automated Crypto Web Scraper/Bitcoin_Price.csv', index = False)

    # Print out the data frame
    print(df)


# Put the above function inside a where loop
# 'time.sleep(60)' makes Python extracts the price of Bitcoin every minute

while True:
    automated_crypto_pull()
    time.sleep(60)
