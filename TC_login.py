from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import requests

def login (driver):

    logo = driver.find_element(By.XPATH, "//div[@class='login_logo']")
    print(f"Welcome to {logo.text}")
    username = "standard_user"
    password = "secret_sauce"
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys(username)
    time.sleep(2)
    password_field.send_keys(password)
    time.sleep(3)

    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
