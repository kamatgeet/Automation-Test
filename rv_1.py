#download chromedriver.exe in the same folder as this script
#this script tests scrolling,if the main tabs are visible even after scrolling,checks the Copyright text,logo of Creditcards.com and the link which takes it back at the top.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium.webdriver.common.by import By

def setUpClass():
    
    driver = webdriver.Chrome('chromedriver.exe')
    driver.fullscreen_window()
    url='https://www.creditcards.com/'
    driver.get(url)
    print(url)
    time.sleep(2)
    #tab1=driver.find_element_by_xpath("/html/body/div[1]/main/section[1]/div[2]/div/label").click()
    #time.sleep(3)
    #tab2=driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div/div/div[2]").click()
    #time.sleep(3)
    driver.execute_script("window.scrollTo(0, 1000)") 
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 4000)")
    time.sleep(6)
    labels = driver.find_elements_by_class_name("menu__item-label")
    for label in labels:
        print(label.text)
    tab1=driver.find_element_by_xpath("/html/body/div[1]/header/nav/ul/li[1]/a").click()
    time.sleep(3)
    tab2=driver.find_element_by_xpath("/html/body/div[1]/header/nav/ul/li[2]/a").click()
    time.sleep(3)
    tab3=driver.find_element_by_xpath("/html/body/div[1]/header/nav/ul/li[3]/a").click()
    time.sleep(3)
    tab4=driver.find_element_by_xpath("/html/body/div[1]/header/nav/ul/li[4]/a").click()
    time.sleep(3)
    time.sleep(3)
    #sublabels = driver.find_elements_by_class_name("cardFinder__tab")
    #for sublabel in sublabels:
        #print(sublabel.text)
    copyright=driver.find_element_by_class_name("footerLegal__copyright").text
    if "Copyright 2019 CreditCards.com. All Rights Reserved" in copyright:
        print(copyright)
        print("Copyright is present and is correct")
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/footer/div[2]/div[2]/div[1]/a/img").click() 
    time.sleep(6)
    
setUpClass()

def tearDown():
    driver.quit()

