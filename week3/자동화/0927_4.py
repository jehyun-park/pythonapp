from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip

browser = webdriver.Chrome("C:/chromedriver.exe")
browser.get("https://www.naver.com")
browser.maximize_window()
time.sleep(1)

login = browser.find_element(By.CSS_SELECTOR,'#account > a')
login.click()
time.sleep(1)

id = browser.find_element(By.ID,"id")
id.click()
#id.send_keys("abcde")

#pyautogui.write("jehyun1590",interval=0.25)  ## 타이핑하듯이 입력
#time.sleep(1)

pyperclip.copy("jehyun1590")
pyautogui.hotkey("ctrl","v")

time.sleep(1)

pw = browser.find_element(By.ID,"pw")
pw.click()
#pw.send_keys("12345")
pyperclip.copy("90551862pjh")
pyautogui.hotkey("ctrl","v")

time.sleep(1)

login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login") #enter = browser.find_element(By.ID,"log.login")
login_btn.click()                                               #enter.click()


'''
time.sleep(2)
id = browser.find_element(By.ID,"id")
id.clear()

id = browser.find_element(By.ID,"id")
id.click()
id.send_keys("edcba")
time.sleep(1)

pw = browser.find_element(By.ID,"pw")
pw.click()
pw.send_keys("54321")
time.sleep(1)
'''