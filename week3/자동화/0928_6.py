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

login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login") 
login_btn.click()                                               
time.sleep(1)

browser.get("https://mail.naver.com/")
time.sleep(1)

### 여기 이상함
browser.find_element(By.CSS_SELECTOR,"#nav_snb > div.btn_workset > a.btn_quickwrite._c1\(mfCore\|popupWrite\|new\)._ccr\(lfw\.write\)._stopDefault > strong > span")
time.sleep(1) 

#pyperclip.copy("wpgus6242@cu.ac.kr")
#pyautogui.hotkey("ctrl","v")
pyautogui.write("jehyun1590@naver.com",interval=0.25)
pyautogui.press("tab")
pyautogui.press("tab")
time.sleep(1)

pyperclip.copy("자동 메일 발송입니다!")
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab")
time.sleep(1)

pyperclip.copy("자동 메일 본문 내용입니다!")
pyautogui.hotkey("ctrl","v")
time.sleep(1)

browser.find_element(By.ID,"sendBtn").click()