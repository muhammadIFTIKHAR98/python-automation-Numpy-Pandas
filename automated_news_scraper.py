import requests
from bs4 import BeautifulSoup

#url of the news website
url = ''

#make a request to the website 
response = response.get(url)

#check if the request was successful
if response.status_code == 200:
    #parse the page content with beautifulsoup
    soup = BeautifulSoup(response.content, 'html.parser')

    #find all headline elements (update this selector based on the actual site)
    headlines = soup.find_all('div', class_='hp-featured-second-stories')

    #store the headline in a list
    news_headlines = [headline.get_text(strip=true) for headline in headlines]

    #print or save the headlines
    for index, headlines in enumerate(news_headlines, 1):
        print(f"{index}. {headline}")
else:
    print("failed to retrieve the webpage")

#file path to store the headlines
file_path = 'file/path/to/save/the/file'

#open the file in append mode and write the headlines
with open(file_path, 'a') as file:
    file.write("latest news headlines:\n")
    file.write("\n".join(news_headlines))
    file.write("\n\n")
