#키보드와 마우스 이벤트 처리
# 이미지 왜 안됨????????????


from dis import show_code
import tkinter.messagebox as msgbox
from tkinter import *

def leftclick(event):
    msgbox.showinfo("마우스", "마우스 왼쪽 버튼을 클릭하였습니다.")

def imageclick(event):
    msgbox.showinfo("마우스","이미지 파일클릭")

window=Tk()
window.geometry("800x640")

photo=PhotoImage(file="week2/sushi.png")
label1 = Label(window,image=photo)
label1.pack(expand=True, anchor=CENTER)

label1.bind("<Button>", imageclick)


#window.bind("<Button-1>",leftclick)   ##Button-1 : 왼쪽 버튼 / Button-2 : 가운데 버튼 / Button-3 : 우측버튼 / Button : 모든 버튼



window.mainloop()