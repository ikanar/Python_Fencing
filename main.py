from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


@dataclass
class Tournament:
    'Class that represents a Tournament'
    name: str
    event_list: []

@dataclass
class Event:
    'Class that represents an Event at a Tournmanent'
    event_name: str
    bout_history: []

@dataclass
class Bout:
    bout_type: str
    result: str
    score: str
    opponent:str
    country: str
    seed: str
    rank: str
    rating: str
    place: str
    club: str
    opponent_strength: str
    strength: str
    change: str
    chance_of_victory: str




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

    for h4,h5 in zip(h4_elements,h5_elements):
        print (h4.text.strip())
        print(h5.a.text.strip())
    

    #there are 14 elements in the tournament table
    bout_history = []
    temp_bout = []

    for table in tables[3:]:
        rows = table.find_all('td')
        
        for row in rows:
            #stores bout elements in temp_bout
            temp_bout.append(row.text.strip())
            
            if(len(temp_bout) == 14):
                #creates bout object, stores the bout in the bout_history list, resets the temp_bout to an empty list
                bout = Bout(temp_bout[0],temp_bout[1],temp_bout[2],temp_bout[3],temp_bout[4],temp_bout[5],temp_bout[6],temp_bout[7],temp_bout[8],temp_bout[9],temp_bout[10],temp_bout[11],temp_bout[12],temp_bout[13])
                bout_history.append(bout)
                temp_bout = []
                print(bout.opponent)
        #sleep(100)


    
    #td_elements = soup.find_all('td')
    #for element in td_elements:
    #      print (element.text)




    