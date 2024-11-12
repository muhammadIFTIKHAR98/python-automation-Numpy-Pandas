#this is the python code of web scraping using the beautifulsoup4 
#this code is from the crash course of youtube channel (free code camp).
#there will be more changes in this code
from bs4  import BeautifulSoup
import requests

print('put some skills that you are not familiar with')
unfamiliar_skill = input('>')
print(f'filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    #print(html_text)
    
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:
        publish_date = job.find('span', class_ = 'sim-posted').span.text
        if "few" in publish_date: 
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
            skill = job.find('div', class_ = 'srp-skills').text.strip()
            skill_list = [s.strip() for s in skill.split('\n') if s.strip()]
            skill_single_line = ','.join(skill_list)
            more_info = job.header.a['href']
            if unfamiliar_skill not in skill:    
                print(f"company name: {company_name}")
                print(f"skills required: {skill_single_line}")
                print(f"more_info: {more_info}")
                print("\n")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes....')
        time.sleep(time_wait * 60)
        
