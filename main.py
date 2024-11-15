from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests




if __name__ == "__main__":
    name = input("Please enter fencer name: ")
    driver = webdriver.Chrome()
    driver.get("https://www.fencingtracker.com")
    driver.find_element(By.XPATH, '//*[@class="navbar-toggler"]').click()
    sleep(1)
    searchbox = driver.find_element(By.XPATH, '//*[@id="searchTextbox"]').send_keys(name + "\n")
    sleep(1)
    
    history_link = driver.find_element(By.LINK_TEXT,"History")
    history_link.click()

    elements = driver.find_elements(By.TAG_NAME,"h4")
    sleep(1)

    html=driver.page_source
    soup = BeautifulSoup(html, features = "html.parser")

    h4_elements = soup.find_all('h4')
    h5_elements = soup.find_all('h5')

    for h4,h5 in zip(h4_elements,h5_elements):
     print (h4.text)
     print(h5.a.text)
     print(h5.text)

    
    #td_elements = soup.find_all('td')
    #for element in td_elements:
    #   if element.a != None:
    #      print (element.text)




    