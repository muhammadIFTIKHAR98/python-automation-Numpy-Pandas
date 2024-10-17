import requests
from bs4 import BeautifulSoup

#url of the webpage to scrape
url = 'https://www.livemint.com/market/market-stats/stocks-tata-steel-share-price-nse-bse-s0003026'

#make an http request to get the content of the page
response = requests.get(url)

#check if the request was successful
if response.status_code == 200:
    print("successfully retrieved the webpage")
    #parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')

    #find the product price by inspecting the webpage's HTML    
    #(this selector will change depending on the website you're scraping)
    price = soup.find('div', class_='priceRange') # keep in mind the tag and class which will fetch the rate or data required.
    if price is not None:
        price = price.text.strip()
        print(f"product price: {price}")
    else:
        print("product price not found")
else:
    print("failed to retrieve the webpage")

import csv

#path to your CSV file
csv_file = '/home/muhammad-iftikhar/ifti/steel_prices.csv'

#open the CSV file and append data
with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([price])

print(f"price {price} saved to CSV")

    
