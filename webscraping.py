from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from time import sleep
import csv
from plyer import notification
from tqdm import tqdm
from selenium import TimeoutException

def execute(input, output, n, alert):
    base_url = 'https://www.reclameaqui.com.br'
    wd = get_web_driver()
    writer = get_output_writer(output)
    lines = [line.rstrip() for line in input] 
    for line in tqdm(lines):
        try:
            print()
            print(f'Searching for {line}...............................................')
            print()
            data = scrap(line, n, base_url, wd)
            save_to_output(writer, data)
        except TimeoutException as ex:
            continue
    if alert == 'y' or alert == True:
        showNotification()
    wd.quit()

def save_to_output(writer, data):
    for i in data:
        #write the rows
        writer.writerow(i)

def get_web_driver():
    wd = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
    return wd

def get_output_writer(output):
    column_names = ['title', 'text']
    f = open(output, 'a', encoding='utf-8') 
    writer = csv.writer(f)
    # write the column names
    writer.writerow(column_names)
    return writer
    
def scrap(name, n, base_url, wd):
    for page in tqdm(range(1, n)):
        print(f'Page {page} of {n}')
        url_site = f'{base_url}/empresa/{name.lower()}/lista-reclamacoes/?pagina={page}'
        wd.get(url_site)
        html = wd.page_source
        bs_obj = bs(html,'html.parser')
        boxes = bs_obj.find_all('div', {'class':'sc-1pe7b5t-0 bJdtis'})

        href_links = [box.find('a').get('href') for box in boxes]
        page_links = [f'{base_url}{link}' for link in href_links]

        for link in page_links:
            wd.get(link)
            sleep(4)
            bs_page = bs(wd.page_source, 'html.parser')
            title = bs_page.find('h1', {'data-testid': 'complaint-title'}).text
            body = bs_page.find('p', {'data-testid':'complaint-description'}).text
            print([title,body])
            yield [title, body]
        
def showNotification(output):
    notification.notify(
        title='Web Scraping Finished',
        message=f'Data collected and save to {output}',
        timeout=10
    )
    
