#this file is not running properly although it seems that code is correct, maybe there is an issue with the extracting the data from website 

import requests
from bs4 import beautifulsoup

#url of the news website
url ='https://www.amazon.in/s?k=iphone&crid=2ZI9M2M6FJRHV&sprefix=%2Caps%2C203&ref=nb_sb_ss_recent_1_0_recent'
#this is used as many website does not allow their data to get extracted by any code.
# I have searched how to simulate a browser and request python.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 

#make a request to the website 
r = requests.get(url, headers=headers)

#check the response status
if r.status_code == 200:
    print("request successful!")
    soup = BeautifulSoup(r.text, 'html.parser')

#print(soup.prettify())
spans = soup.select( "span.a-size-medium")
for span in spans:
    print(span.string)
