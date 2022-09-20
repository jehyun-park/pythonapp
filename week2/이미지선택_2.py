
from tkinter import *


window=Tk()
window.geometry("1024x768")

def pic_btn():
    if var.get() == 1 :
        labelimage.configure(image=photo1)
    elif var.get() == 2:
        labelimage.configure(image=photo2)
    elif var.get() == 3:
        labelimage.configure(image=photo3)
    else:
        labelimage.configure(image=photo4)

labelText = Label(window,text="보고싶은 사진을 선택하세요.")
labelText.pack()

var = IntVar()
opt1 = Radiobutton(window,text="고양이", variable=var,value=1)
opt1.pack(padx=5,pady=5)

opt2 = Radiobutton(window,text="고릴라", variable=var,value=2)
opt2.pack(padx=5,pady=5)

opt3 = Radiobutton(window,text="펭귄", variable=var,value=3)
opt3.pack(padx=5,pady=5)

opt4 = Radiobutton(window,text="다람쥐", variable=var,value=4)
opt4.pack(padx=5,pady=5)

btn_s = Button(window,text = "사진 보기",command=pic_btn)
btn_s.pack()

photo1 = PhotoImage(file="week2/cat.png")
photo2 = PhotoImage(file="week2/gorilla.png")
photo3 = PhotoImage(file="week2/penguin.png")
photo4 = PhotoImage(file="week2/squirrel.png")

labelimage = Label(window,width=400,height=400,bg="yellow")
labelimage.pack()


window.mainloop()