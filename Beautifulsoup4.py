#this is the file in which i am learning the beautifulsoup4, its function and how to do web scraping
from bs4 import BeautifulSoup
import requests

url = 'https://www.newegg.com/gigabyte-gv-n4090gaming-oc-24gd-nvidia-geforce-rtx-4090-24gb-gddr6x/p/N82E16814932550'
result = requests.get(url)
#print(result.text)

doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())


# prices = doc.find_all(text="$")
# print(prices)


# prices = doc.find_all(text="$")
# parents = prices[0].parent
# print(parents)

# print(prices)
# this is showing an error in my code but works fine in tutorial

# prices = doc.find_all(string="$")
# print(prices)
# this is used in place of above portion here "text" is replaced by "string"

#creating variable
# prices = doc.find_all("ul", class_="price") 
# print(prices)

# #check if the price element was found and print the price
# if prices:
#     print("price found:", prices.get_text(strong=True))

# else:
#     print("price not found.")
