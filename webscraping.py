from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options

from time import sleep
import csv
from plyer import notification
from tqdm import tqdm


def execute(input, output, n, alert):
    base_url = 'https://www.reclameaqui.com.br'
    writer = get_output_writer(output)
    lines = [line.rstrip() for line in input] 
    for line in tqdm(lines):
        print()
        print(f'Searching for {line}...............................................')
        print()
        data = scrap(line, n, base_url)
        save_to_output(writer, data)
    if alert == 'y' or alert == True:
        showNotification(output)

def save_to_output(writer, data):
    for i in data:
        #write the rows
        writer.writerow(i)

def get_web_driver():
    options = webdriver.FirefoxOptions()
    # wait until the initial HTML document has been completely loaded and parsed
    options.page_load_strategy = 'eager'
    wd = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    return wd

def get_output_writer(output):
    column_names = ['title', 'text']
    f = open(output, 'a', encoding='utf-8') 
    writer = csv.writer(f)
    # write the column names
    writer.writerow(column_names)
    return writer
    
def scrap(name, n, base_url):
    notification.notify(title='Web Scraping',message=f'Collecting data from {name}',timeout=10)
    content = []
    wd = get_web_driver()
    for page in range(2, (2+n)):
        print(f'\nPage {page} of {(2 + n)}')
        print()
        url_site = f'{base_url}/empresa/{name.lower()}/lista-reclamacoes/?pagina={page}'
        wd.get(url_site)
        sleep(3)
        source = wd.page_source
        bs_obj = bs(source,'html.parser')
        boxes = bs_obj.find_all('div', {'class':'sc-1pe7b5t-0 bJdtis'})

        href_links = [box.find('a').get('href') for box in boxes]
        page_links = [f'{base_url}{link}' for link in href_links]
        
        print('----------------------------------------------------------\n')
        print('Content \n')

        for link in page_links:
            try:
                print(f'Link: {link}')
                wd.get(link)
                sleep(2)
                bs_page = bs(wd.page_source, 'html.parser')
                title = bs_page.find('h1', {'data-testid': 'complaint-title'}).text
                body = bs_page.find('p', {'data-testid':'complaint-description'}).text
                print(f'Title: {title} \nBody: {body[:80]}')
                print('-----------------------------------------------------------------------------\n')
                yield [title, body]
                #content.append([title, body])
            except WebDriverException as wd:
                continue
            except Exception as e:
                notification.notify(
                    title='Web Scraping',
                    message=f'Exception: {e}',
                    timeout=10
                )
                print(e)
    wd.quit()
    return content
        
def showNotification(output):
    notification.notify(
        title='Web Scraping',
        message=f'Data collected and saved to {output}',
        timeout=10
    )
    
