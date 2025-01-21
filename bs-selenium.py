from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#set up the chromedriver path
driver_path = '/home/snap/chromium/chromedriver-linux64/chromedriver'  #replace with the path to your chromedriver

#initialize chrome service
service = Service(driver_path)
#initialize the browser (chrome in this case)
driver = webdriver.Chrome(service=service)

try:
    #open the website
    url = 'https://www.thehindu.com/news/international/'
    driver.get(url)

    #pause briefly to let the page load
    time.sleep(3)

    #find all headline elements (update this selector based on the websites's structure)
    headlines = driver.find_elements(BY.CLASS_NAME, 'title big') #use actual class from the website

    #extract and print each headline's text
    news_headline = [headline.text for headline in headlines]

    #save the headlines to a file
    file_path = '/home/muhammad-iftikhar/python-files/news_headlines_selenium.txt'
    with open(file_path, 'a') as file:
        file.write("latest news headlines:\n")
        file.write("\n".join(news_headlines))
        file.write("\n\n")
    
    #print confirmation
    print("headlines saved successfully!")

except Exception as e:
    print(f"an error occured: {e}")

finally:
    #close the browser
    driver.quit()