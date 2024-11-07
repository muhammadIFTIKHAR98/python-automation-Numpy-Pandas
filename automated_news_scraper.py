import requests
from bs4 import BeautifulSoup

#url of the news website
url = 'websiteurl@example.com'

#make a request to the website 
response = requests.get(url)

#check if the request was successful
if response.status_code == 200:
    #parse the page content with beautifulsoup
    soup = BeautifulSoup(response.content, 'html.parser')

    #find all headline elements (update this selector based on the actual site)
    #you may need to adjust the class name based on the current structure of the website
    headlines = soup.find_all('div', class_='hp-featured-second-stories') #example class, adjust as needed

    #store the headline in a list with timestamp
    news_headlines = []
    for headline in headlines:
        text = headline.get_text(strip=True)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        news_headlines.append(f"{timestamp} - {text}")

    #print or save the headlines
    for index, headlines in enumerate(news_headlines, 1):
        print(f"{index}. {headline}")
    
    #file path to store the headlines
    file_path = 'file/path/to/store/the/headlines/filetype/will/be/.txt/file'

    #open the file in append mode and write the headlines
    with open(file_path, 'a') as file: #changed the 'w' to 'a' to append
        for headline in news_headlines:
            file.write(headline + '\n') #write each headline on a new line
    
else:
    print("failed to retrieve the webpage")
