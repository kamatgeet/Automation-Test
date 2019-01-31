#download chromedriver.exe in the same folder as this script
#checks all the links on the website

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium.webdriver.common.by import By

def setUpClass():

    driver = webdriver.Chrome('chromedriver.exe')
    url='https://www.creditcards.com/'
    driver.get(url)
    print(url)
    time.sleep(3)
    links = driver.find_elements_by_css_selector("a")
    for link in links:
        r = requests.head(link.get_attribute('href'))
        print(link.get_attribute('href'), r.status_code)	
    time.sleep(3)
    
setUpClass()

def tearDown():
    driver.quit()
	
	
