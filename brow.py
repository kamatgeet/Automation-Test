#download chromedriver.exe and geckodriver.exe in the same folder as this script

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium.webdriver.common.by import By

def setUpClass(driver):
    
    
    driver.fullscreen_window()
    url='https://www.creditcards.com/'
    driver.get(url)
    print(url)
    time.sleep(3)
    labels = driver.find_elements_by_class_name("menu__item-label")
    for label in labels:
        print(label.text)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 1000)") 
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 4000)")
    time.sleep(3)
    driver.close()
 
 
setUpClass(webdriver.Chrome('chromedriver.exe'))

setUpClass(webdriver.Firefox())

def tearDown():
    driver.quit()
	
