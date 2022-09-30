import pyautogui

#for w in pyautogui.getAllWindows(): #모든 윈도우 가져오기
#    print(w)


#for w in pyautogui.getWindowsWithTitle("제목 없음"):
#    print(w)
    
#    if w.isActive == False:  #현재 활성화가 되지않았다면
#        w.activate()        #활성화 시켜라

1
#    if w.isMaximized == False: #현재 최대크기가 아니라면
#        w.maximize()            #최대크기로해라
#
#    if w.isMinimized == False:  #현재 최소크기가 아니라면
#        w.minimize()            #최소크기


for w in pyautogui.getWindowsWithTitle("제목 없음"):
    w.activate()
   
    pyautogui.sleep(1)
    #pyautogui.write("12345")
    #pyautogui.write("Daegu",interval=0.25)

    #pyautogui.write(["t","e","s","t","left","right","1","enter"],interval=0.25)
    #pyautogui.keyDown("shift")
    #pyautogui.press("$")
    #pyautogui.keyUp("shift")

    #pyautogui.keyDown("ctrl")
    #pyautogui.keyDown("a")
    #pyautogui.keyUp("a")
    #pyautogui.keyUp("ctrl")

    pyautogui.mouseInfo()  #마우스좌표확인
    pyautogui.hotkey("ctrl","a")


