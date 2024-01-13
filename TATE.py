from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://finance.yahoo.com/quote/TATATECH.BO?p=TATATECH.BO&.tsrc=fin-srch")
print(driver.title)
time.sleep(5)

#opening historical data tab
element = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-test='HISTORICAL_DATA']"))
)
element.click()
time.sleep(5)

# date=[]
# open=[]
# high=[]
# low=[]
# close=[]
# ajd_close=[]
# volume=[]

table = driver.find_elements(By.CSS_SELECTOR, "table[data-test='historical-prices']")
# table = driver.find_elements(By.TAG_NAME, "td")
for cell in table:
    print(cell.text)
    # date.append(cell.find_element(By.XPATH('./td[1]').text))
time.sleep(5)

df = pd.DataFrame({'TATA TECH':cell})
df.to_csv('Stock_value', index=False)
print(df)

time.sleep(5)
driver.quit()