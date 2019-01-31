#download chromedriver.exe in the same folder as this script
#Checks the tabs are present or not

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium.webdriver.common.by import By

def setUpClass():
    
    driver = webdriver.Chrome('chromedriver.exe')
    driver.fullscreen_window()
    #driver.set_window_size(300, 500)
    url='https://www.creditcards.com/'
    driver.get(url)
    print(url)
    time.sleep(3)
    labels = driver.find_elements_by_class_name("menu__item-label")
    for label in labels:
        print(label.text)

    tab1=driver.find_element_by_xpath("/html/body/div[1]/header/nav/ul/li[1]/a").text
    if "Card Category" in tab1: 
        tab1=driver.find_element_by_xpath("/html/body/div[1]/header/nav/ul/li[1]/a").click()
        print("Card Category present")
        time.sleep(3)
    else:
        print("Card Category not present")
    
    
    tab2=driver.find_element_by_xpath("/html/body/div[1]/header/nav/ul/li[2]/a").text
    if "Card Issuer" in tab2:
        tab2=driver.find_element_by_xpath("/html/body/div[1]/header/nav/ul/li[2]/a").click()
        print("Card Issuer is presnt")
        time.sleep(3)
    else:
        print("Card Issuer is not present")
	
    tab3=driver.find_element_by_xpath("/html/body/div[1]/header/nav/ul/li[3]/a").text
    if "Credit Range" in tab3:
        tab3=driver.find_element_by_xpath("/html/body/div[1]/header/nav/ul/li[3]/a").click()
        print("Credit Range is presnt")
        time.sleep(3)
    else:
        print("Credit Range is not present")
		
    tab4=driver.find_element_by_xpath("/html/body/div[1]/header/nav/ul/li[4]/a").text
    if "Resources" in tab4:
        tab4=driver.find_element_by_xpath("/html/body/div[1]/header/nav/ul/li[4]/a").click()
        print("Resources is presnt")
        time.sleep(3)
    else:
        print("Resources is not present")		


setUpClass()

def tearDown():
    driver.quit()
	
 