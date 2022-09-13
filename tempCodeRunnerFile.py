from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver

wd = webdriver.Chrome()
wd.get("https://www.reclameaqui.com.br/empresa/ifood/")
html = wd.page_source
page = bs(html,'html.parser')