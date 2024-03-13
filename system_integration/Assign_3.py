# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Walmart homepage
driver.get("https://www.sobeys.com/en/")
time.sleep(8)

# Clicking on "Services" from the homepage
recipes_link = driver.find_element(By.XPATH, "/html/body/header/div[3]/div/div/div/div[2]/div/div/div/div/div/nav/div/ul/li[4]/a")
recipes_link.click()
time.sleep(5)

# Clicking on "Financial Services" from the services page
about_us_link = driver.find_element(By.XPATH, "/html/body/header/div[3]/div/div/div/div[2]/div/div/div/div/div/nav/div/ul/li[7]/button")
about_us_link.click()
time.sleep(7)

# Clicking on "Gift Cards" from financial services page
learn_more_link = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/main/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div/a")
learn_more_link.click()
time.sleep(5)

# Clicking on "Buy Now" for a gift card
entertaining_platters_link = driver.find_element(By.XPATH, "/html/body/header/div[3]/div/div/div/div[2]/div/div/div/div/div/nav/div/ul/li[6]/a")
entertaining_platters_link.click()
time.sleep(5)

home_link = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/main/div/div[5]/div/div/div/div/div/div/div/div/div/nav/ol/li[1]/a")
home_link.click()
time.sleep(5)

# Displaying the output
print ("Successfully completed the check flow: **Opened the homepage**, **clicked on recipes**, **go to the about us page**, **clicked on entertaining platters**,  **proceeded back to home page **")

# Closing the webdriver
driver.close()
