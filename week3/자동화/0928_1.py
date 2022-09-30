import pyautogui

'''
size = pyautogui.size()  # 현재 화면의 스크린 사이즈
print(size)

pyautogui.moveTo(200,100)  # 마우스 절대 좌표로 이동
pyautogui.moveTo(100,200,duration=5) # 마우스가 5초동안 해당좌표로 이동
'''
pyautogui.moveTo(100,100, duration=0.25)
p = pyautogui.position()
print(p[0],p[1])
print(p.x,p.y)

'''
pyautogui.moveTo(200,200, duration=0.5)
pyautogui.moveTo(300,300, duration=0.75)
pyautogui.moveTo(400,400, duration=1.0)
'''
pyautogui.move(100,100, duration=0.5) # 상대 좌표로 마우스 이동
print(pyautogui.position())
pyautogui.move(100,100, duration=0.75)
print(pyautogui.position())




