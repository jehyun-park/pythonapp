from pickletools import optimize
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip

#from selenium.webdriver.chrome.options import Options    

#options = webdriver.ChromeOptions()        //전체화면
#options.add_argument('--start-fullscreen')
#--window-size=x,y/ --start-maximized / --mute-audio (음소거)

browser = webdriver.Chrome("C:/chromedriver.exe")#,chrome_options=options)
browser.get("https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/")
browser.maximize_window()
time.sleep(1)

id = browser.find_element(By.ID,"id")
id.click()

pyperclip.copy("jehyun1590")
pyautogui.hotkey("ctrl","v")

time.sleep(1)

pw = browser.find_element(By.ID,"pw")
pw.click()
pyperclip.copy("90551862pjh")
pyautogui.hotkey("ctrl","v")
time.sleep(1)

login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login") 
login_btn.click()                                               
time.sleep(1)

browser.get("https://m.blog.naver.com/FeedList.naver")
time.sleep(1)

browser.get("https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FFeedList.naver")
time.sleep(3)

title = browser.find_element(By.CSS_SELECTOR,"#se_component_wrapper > div:nth-child(1) > div > div.se_sectionArea.se_align-left > div > div > div > div > textarea")
title.click()
time.sleep(1)

#pyperclip.copy("네이버 블로그 제목")
#pyautogui.hotkey("ctrl","v")
title.send_keys("[현장포토] '조각상, 여기있어'...휘인, 완벽한 포즈")
time.sleep(2)

memo = browser.find_element(By.CSS_SELECTOR,"#se_component_wrapper > div:nth-child(2) > div > div > div > div.se_viewArea.se_ff_nanumgothic.se_align-left.se_fs_T3 > div > div > div > div")
memo.click()
#pyperclip.copy("네이버 블로그 내용")
#pyautogui.hotkey("ctrl","v")
memo.send_keys("JTBC 예능프로그램 '아는 형님' 출근길 포토타임이 29일 오전 경기도 고양시 JTBC 일산 스튜디오에서 진행됐다.\n휘인은 남다른 포즈를 뽐냈다. 조각상같은 모습이 시선을 끌었다.")
memo.send_keys(Keys.ENTER)
memo.send_keys("체리피스 자매 (휘인, 화사)")
time.sleep(2)

submit = browser.find_element(By.CLASS_NAME,"btn_applyPost")
submit.click()
time.sleep(2)
