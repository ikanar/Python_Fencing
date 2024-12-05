from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests




if __name__ == "__main__":
    #get input from user
    name = input("Please enter fencer name: ")
   
   
   
   #initialize webdriver and navigate to the users page, utilizes sleeps so that the searchbar has time to load
    driver = webdriver.Chrome()
    driver.get("https://www.fencingtracker.com")
    driver.find_element(By.XPATH, '//*[@class="navbar-toggler"]').click()
    sleep(1)


    searchbox = driver.find_element(By.XPATH, '//*[@id="searchTextbox"]').send_keys(name + "\n")
    sleep(1)
    
    history_link = driver.find_element(By.LINK_TEXT,"History")
    history_link.click()


    #scrape elements from page
    elements = driver.find_elements(By.TAG_NAME,"h4")
    sleep(1)

    html=driver.page_source
    soup = BeautifulSoup(html, features = "html.parser")

    h4_elements = soup.find_all('h4')
    h5_elements = soup.find_all('h5')
    tables = soup.find_all('tbody',{'class','table-group-divider'})

   # for h4,h5 in zip(h4_elements,h5_elements):
   #  print (h4.text)
   #  print(h5.a.text)
   #  print(h5.text)
    

    #there are 14 elements in the tournament table

    for table in tables[3:]:
        rows = table.find_all('td')
        for row in rows[1:]:
            print (row.text.strip())
        sleep(100)

    
    #td_elements = soup.find_all('td')
    #for element in td_elements:
    #      print (element.text)




    