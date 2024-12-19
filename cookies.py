from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/ ')

time.sleep(2)

cookie = driver.find_element(By.CSS_SELECTOR, value='#cookie')
cookie_per_second = driver.find_element(By.CSS_SELECTOR, value='#cps')

def buy():
    store = driver.find_elements(By.CSS_SELECTOR, value='#store > *')
    for i in range(len(store)-2, -1, -1):
        if store[i].get_attribute('class') != 'grayed':
            store[i].click()
            break

timeout = time.time() + 60*5
def settimer():
    return time.time() + 5

timer = settimer()
while True:
    if time.time() > timeout:
        print(cookie_per_second.text)
        break
    else:
        if time.time() > timer:
            buy()
            timer = settimer()
        else:
            cookie.click()
