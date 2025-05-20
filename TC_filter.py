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
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

login(driver)

homepage = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
print(homepage.text)
driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]').click()
time.sleep(2)
highest = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div')
print(f"Barang termahal adalah: {highest.text}")
driver.save_screenshot("highest.png")
driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]').click()
time.sleep(2)
lowest = driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
print(f"Barang termurah adalah: {lowest.text}")
driver.save_screenshot("lowest.png")
driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]').click()
time.sleep(2)
desc = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div')
print(f"Berdasarkan descending :{desc.text}")
driver.save_screenshot("desc.png")
driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]').click()
time.sleep(2)
asc = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
print(f"Berdasarkan ascending:{asc.text}")
driver.save_screenshot("asc.png")

driver.quit()
