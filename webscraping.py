from operator import add
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
import click

def showNotification(output):
    notification.notify(
        title='Web Scraping',
        message=f'Data collected and saved to {output}',
        timeout=10
    )
    
def add_headings(output):
    with open(output, 'r') as f:
        reader = csv.reader(f)
        csv_headings = next(reader)
        if 'title' not in csv_headings[0]:
            with open(output, 'a', encoding='utf-8') as f:
                column_names = ['title', 'body']
                writer = csv.writer(f) 
                writer.writerow(column_names)
            
def save_to_output(output, data):
    with open(output, 'a', encoding='utf-8') as f:
        writer = csv.writer(f) 
        for i in data:
            #write the rows
            writer.writerow(i)
    click.echo('Successful saved to output')

def get_web_driver():
    options = webdriver.FirefoxOptions()
    # wait until the initial HTML document has been completely loaded and parsed
    options.page_load_strategy = 'eager'
    wd = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    return wd

def get_content(wd, page_links, output):
    contents = []
    for link in page_links:
            try:
                click.echo(f'Link: {link}')
                wd.get(link)
                sleep(2)
                bs_page = bs(wd.page_source, 'html.parser')
                title = bs_page.find('h1', {'data-testid': 'complaint-title'}).text
                body = bs_page.find('p', {'data-testid':'complaint-description'}).text
                click.echo(f'Title: {title} \nBody: {body[:80]}')
                click.echo('-----------------------------------------------------------------------------\n')
                if title == '':
                    break
                contents.append([title, body])
            except WebDriverException as wd:
                continue
            except Exception as e:
                notification.notify(
                    title='Web Scraping',
                    message=f'Exception: {e}',
                    timeout=10
                )
                click.echo(e)
    save_to_output(output, contents)
    
def scrap(output, name, n, start_from, base_url):
    notification.notify(title='Web Scraping',message=f'Collecting data from {name}',timeout=10)
    total_page = n + start_from
    for page in range(start_from, total_page):
        click.echo(f'\nPage {page} of {total_page}')
        click.echo()
        url_site = f'{base_url}/empresa/{name.lower()}/lista-reclamacoes/?pagina={page}'
        wd = get_web_driver()
        wd.get(url_site)
        sleep(3)
        source = wd.page_source
        bs_obj = bs(source,'html.parser')
        boxes = bs_obj.find_all('div', {'class':'sc-1pe7b5t-0 bJdtis'})

        href_links = [box.find('a').get('href') for box in boxes]
        page_links = [f'{base_url}{link}' for link in href_links]
        
        click.echo('----------------------------------------------------------\n')
        click.echo('Content \n')
        get_content(wd, page_links, output)
        wd.quit()

def execute(input, output, n, start_from, alert):
    base_url = 'https://www.reclameaqui.com.br'
    add_headings(output)
    lines = [line.rstrip() for line in input] 
    for line in tqdm(lines):
        click.echo()
        click.echo(f'Searching for {line}...............................................')
        click.echo()
        scrap(output, line, n, start_from, base_url)
    if alert == 'y' or alert == True:
        showNotification(output)
       
    
