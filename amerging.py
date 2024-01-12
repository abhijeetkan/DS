from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)

search_box = driver.find_element("name", "q")
search_box.send_keys('amerging technologies')
search_box.submit()
print("Search successful")
time.sleep(3)

print("finding link")
try:
    first_link = driver.find_element(By.CSS_SELECTOR, "h3")  # Assuming h3 is the tag for the link title
    first_link.click()
    print("Clicked on the first link.")
except Exception as e:
    print("Unable to click on the first link:", str(e))

time.sleep(3)
driver.back()

time.sleep(7)

