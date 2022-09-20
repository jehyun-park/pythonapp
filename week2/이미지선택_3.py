from tkinter import*


file_list = ["week2/dog.png","week2/cat.png","week2/gorilla.png","week2/penguin.png","week2/squirrel.png","week2/sushi.png"]

num = 0

def clickPrev():
    global num
    num -= 1
    if num < 0 :
        num = 6
    photo = PhotoImage(file=file_list[num])
    label1.configure(image=photo)
    label1.image = photo


def clickNext():
    global num
    num +=1
    if num > 6:
        num=0

    photo = PhotoImage(file=file_list[num])
    label1.configure(image=photo)
    label1.image = photo
    


window = Tk()
window.geometry("1920x1280")
window.title = ("사진앨범")

btnPrev = Button(window,text="<< 이전",command=clickPrev)
btnPrev.place(x=400,y=20)

btnNext = Button(window, text=">> 다음", command=clickNext)
btnNext.place(x=600,y=20)

photo = PhotoImage()
label1 = Label(window,image=photo)
label1.place(x=15,y=50)

photo = PhotoImage(file = file_list[0])
label1 = Label(window, image=photo)
label1.pack(expand=True, anchor=CENTER)



window.mainloop()