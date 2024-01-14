from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://finance.yahoo.com/quote/TATATECH.BO?p=TATATECH.BO&.tsrc=fin-srch")
print(driver.title)
time.sleep(3)
#opening historical data tab
element = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-test='HISTORICAL_DATA']"))
)
element.click()
time.sleep(3)

date=[]
open=[]
high=[]
low=[]
close=[]
adj_close=[]
volume=[]

print("finding tabel")
# stocks = driver.find_elements(By.TAG_NAME, 'tr')
rows = driver.find_elements(By.XPATH, '//tr[@class="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"]')
for history in rows:
    # date.append(history.find_element(By.XPATH,'./td[1]').text)
    dt = history.find_element(By.XPATH,'./td[1]').text
    date.append(dt)
    print(dt)
    opn = history.find_element(By.XPATH,'./td[2]').text
    open.append(opn)
    print(opn)
    hi = history.find_element(By.XPATH,'./td[3]').text
    high.append(hi)
    print(hi)
    lo = history.find_element(By.XPATH,'./td[4]').text
    low.append(lo)
    print(lo)
    cl = history.find_element(By.XPATH,'./td[5]').text
    close.append(cl)
    print(cl)
    adj = history.find_element(By.XPATH,'./td[6]').text
    adj_close.append(adj)
    print(adj)
    vol = history.find_element(By.XPATH,'./td[7]').text
    volume.append(vol)
    print(vol)
    # print(history.text)


df = pd.DataFrame({'date': date, 'open': open, 'high': high, 'low': low, 'close': close, 'adj_close': adj_close, 'volume': volume})
df.to_csv('TATE.csv', index=False)
print(df)

time.sleep(3)
driver.quit()
