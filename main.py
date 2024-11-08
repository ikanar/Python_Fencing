from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




if __name__ == "__main__":
    name = input("Please enter fencer name: ")
    driver = webdriver.Chrome()
    driver.get("https://www.fencingtracker.com")
    driver.find_element(By.XPATH, '//*[@class="navbar-toggler"]').click()
    sleep(3)
    searchbox = driver.find_element(By.XPATH, '//*[@id="searchTextbox"]').send_keys(name + "\n")
    sleep(3)
    
    history_link = driver.find_element(By.LINK_TEXT,"History")
    history_link.click()
    print(driver.current_url)

    sleep(4)



    