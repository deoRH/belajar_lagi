from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import requests
from TC_login import login


options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

login(driver)

homepage = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
print(homepage.text)
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(5)
driver.find_element(By.ID, "about_sidebar_link").click()
time.sleep(2)
driver.back()
time.sleep(3)
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(5)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(2)
driver.quit()