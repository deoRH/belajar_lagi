from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import requests

def order (driver):
    driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()
    time.sleep(5)
    Product_name = driver.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    Product_description = driver.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[2]')
    Product_price = driver.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[3]')
    driver.save_screenshot("Product_1.png")
    print(f"Product ini adalah {Product_name.text}")
    print(f"Penjelasan sebagai berikut : {Product_description.text}")
    print(f"Dengan harga satuan sebesar : {Product_price.text}")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="remove"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart"]').click()
    jumlah_cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    print(f"Pembelian sebanyak : {jumlah_cart.text}")
    time.sleep(2)
    driver.find_element(By.ID, 'back-to-products').click()
    time.sleep(2)

    element = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    driver.execute_script("arguments[0].scrollIntoView()",element)
    time.sleep(2)

    Product2_name = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div')
    Product2_description = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[1]/div')
    Product2_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div')
    driver.save_screenshot("Product_2.png")
    print(f"Product ini adalah {Product2_name.text}")
    print(f"Penjelasan sebagai berikut : {Product2_description.text}")
    print(f"Dengan harga satuan sebesar : {Product2_price.text}")
    time.sleep(2)
    driver.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)').click()
    time.sleep(2)

    element = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[1]/div[2]/div')
    driver.execute_script("arguments[0].scrollIntoView()",element)
    time.sleep(2)