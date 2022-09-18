from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from time import sleep
import csv

def execute(name, total):
    base_url = 'https://www.reclameaqui.com.br'
    rows = []
    wd = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

    for page in range(1,total):
        url_site = f'{base_url}/empresa/{name}/lista-reclamacoes/?pagina={page}'
        wd.get(url_site)
        html = wd.page_source
        bs_obj = bs(html,'html.parser')
        boxes = bs_obj.find_all('div', {'class':'sc-1pe7b5t-0 bJdtis'})

        href_links = [box.find('a').get('href') for box in boxes]
        page_links = [f'{base_url}{link}' for link in href_links]

        for link in page_links:
            wd.get(link)
            sleep(3)
            bs_page = bs(wd.page_source, 'html.parser')
            title = bs_page.find('h1', {'data-testid': 'complaint-title'}).text
            body = bs_page.find('p', {'data-testid':'complaint-description'}).text
            print([title,body])
            rows.append([title, body])
    save(rows)
    wd.quit()

def save(rows):
    column_names = ['Title', 'Body']
    with open('./results/web_scraping_results.csv', 'w', encoding='utf-8') as _f:
        writer = csv.writer(_f)
        # write the column names
        writer.writerow(column_names)
        #write the rows
        writer.writerows(rows)


