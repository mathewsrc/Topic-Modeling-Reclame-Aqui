from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from time import sleep

business_name = 'ifood'
base_url = 'https://www.reclameaqui.com.br'
url_site = f'{base_url}/empresa/{business_name}/lista-reclamacoes/'
wd = webdriver.Firefox()
wd.get(url_site)
html = wd.page_source
page = bs(html,'html.parser')
boxes = page.find_all('div', {'class':'sc-1pe7b5t-0 bJdtis'})

href_links = [box.find('a').get('href') for box in boxes]
page_links = [f'{base_url}{link}' for link in href_links]

data = []
for link in page_links:
    wd.get(link)
    sleep(2)
    bs_page = bs(wd.page_source, 'html.parser')
    title = bs_page.find('h1', {'data-testid': 'complaint-title'}).text
    body = bs_page.find('p', {'data-testid':'complaint-description'}).text
    data = (title, body)
print(data[1:10])
wd.quit()