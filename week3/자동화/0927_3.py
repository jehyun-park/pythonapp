from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


url="https://www.naver.com"

browser = webdriver.Chrome("C:/chromedriver.exe")
browser.get(url)
time.sleep(2)

login = browser.find_element(By.CLASS_NAME,'link_login')
login.click()
time.sleep(2)
browser.back()
'''
time.sleep(2)
browser.forward()
time.sleep(2)
browser.refresh()
time.sleep(2)
browser.back()
'''

time.sleep(2)
search = browser.find_element(By.ID,'query')
search.send_keys("대구가톨릭대학교")
time.sleep(1)
search.send_keys(Keys.ENTER)

'''
q = browser.find_element(By.TAG_NAME,'a')
print(q)
'''
time.sleep(1)
browser.get("https://www.daum.net")
search1 = browser.find_element(By.NAME,'q')
search1.send_keys("오늘 날씨")
time.sleep(1)
search1 = browser.find_element(By.XPATH,"//*[@id='daumSearch']/fieldset/div/div/button[3]")
search1.click()
time.sleep(1)
browser.quit()

