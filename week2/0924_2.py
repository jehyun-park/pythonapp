from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("C:\chromedriver.exe")
#웹사이트열기
browser.get('http://www.youtube.com')

#browser.implicitly_wait(10) #로딩될때까지 10초간 기다려 !

time.sleep(2)

search = browser.find_element(By.CSS_SELECTOR,'search-form')
search.click()



'''
#검색창
search = browser.find_element(By.CSS_SELECTOR,"input._searchInput_search_text_3CUDs")
search.click()

#검색 단어 입력
search.send_keys('프라이탁')
search.send_keys(Keys.ENTER)
'''