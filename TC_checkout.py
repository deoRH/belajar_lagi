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
from TC_order import order

options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

login(driver)
order(driver)

driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
time.sleep(8)
driver.find_element(By.ID, "checkout").click()

first_name = "Johnny"
last_name = "Robertson"
zip_code = "10000"

first_name_field = driver.find_element(By.ID, "first-name").send_keys(first_name)
last_name_field = driver.find_element(By.ID, "last-name").send_keys(last_name)
zip_code_field = driver.find_element(By.ID, "postal-code").send_keys(zip_code)

print(f"Nama pelanggan :{first_name}{last_name}")
print(f"Postal code {zip_code}")

time.sleep(5)

driver.find_element(By.ID, "continue").click()

time.sleep(8)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
)

items = driver.find_elements(By.CLASS_NAME, "cart_item")

for item in items:
    name_product = item.find_element(By.CLASS_NAME, "inventory_item_name").text
    name_desc = item.find_element(By.CLASS_NAME, "inventory_item_desc").text
    qty = item.find_element(By.CLASS_NAME, "cart_quantity").text
    price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Nama Barang {name_product}")
    print(f"Deskripsi {name_desc}")
    print(f"Jumlah {qty}")
    print(f"Harga Barang {price}")
    print("-"*50)

subtotal = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
tax = driver.find_element(By.CLASS_NAME, "summary_tax_label").text
total = driver.find_element(By.CLASS_NAME, "summary_total_label").text

print(subtotal)
print(tax)
print(total)

time.sleep(5)
driver.save_screenshot("total.png")
element = driver.find_element(By.ID, "finish")
driver.execute_script("arguments[0].scrollIntoView()",element)
time.sleep(3)
driver.find_element(By.ID, "finish").click()
time.sleep(5)

confirmation_1 = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2').text
confirmation_2 = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/div').text
print(confirmation_1)
print(confirmation_2)

driver.save_screenshot("success.png")

driver.find_element(By.ID, "back-to-products").click()
time.sleep(5)

driver.quit()