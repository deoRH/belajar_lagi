from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import requests

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

logo = driver.find_element(By.XPATH, "//div[@class='login_logo']")
print(f"Welcome to {logo.text}")
username = "no user"
password = "no_user"
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
username_field.send_keys(username)
time.sleep(2)
password_field.send_keys(password)
time.sleep(3)

driver.find_element(By.ID, "login-button").click()
time.sleep(3)

try:
    error_element = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
    error_element = error_element.text
    print(error_element)
except:
    print("Error message not found")

driver.quit()
