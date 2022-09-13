from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import csv
import os

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

business_name = 'amazon'
base_url = 'https://www.reclameaqui.com.br'
url_site = f'{base_url}/empresa/{business_name}/lista-reclamacoes/'
wd = webdriver.Firefox(service=FirefoxService(GeckoDriverManager(path = r".\\Drivers").install()), options=options, service_log_path=os.devnull)
wd.get(url_site)
html = wd.page_source
page = bs(html,'html.parser')
boxes = page.find_all('div', {'class':'sc-1pe7b5t-0 bJdtis'})

href_links = [box.find('a').get('href') for box in boxes][:10]
page_links = [f'{base_url}{link}' for link in href_links][:10]

column_names = ['Title', 'Body']
rows = []
for link in page_links:
    wd.get(link)
    sleep(2)
    bs_page = bs(wd.page_source, 'html.parser')
    title = bs_page.find('h1', {'data-testid': 'complaint-title'}).text
    body = bs_page.find('p', {'data-testid':'complaint-description'}).text
    rows.append([title, body])

with open('results/web_scraping_results.csv', 'w') as _f:
    writer = csv.writer(_f)
    # write the column names
    writer.writerow(column_names)
    #write the rows
    writer.writerows(rows)

wd.quit()