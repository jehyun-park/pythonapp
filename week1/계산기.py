from tkinter import *

window=Tk()
window.title("계산기")

entry_box = Entry(window,width=30, borderwidth=5)
entry_box.grid(row=0,column=0,columnspan=4)

btn_7 = Button(window,text="7", padx=25,pady=15)
btn_8 = Button(window,text="8", padx=25,pady=15)
btn_9 = Button(window,text="9", padx=25,pady=15)
btn_x = Button(window,text="X", padx=25,pady=15)

btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)
btn_x.grid(row=1,column=3)

btn_4 = Button(window,text="4", padx=25,pady=15)
btn_5 = Button(window,text="5", padx=25,pady=15)
btn_6 = Button(window,text="6", padx=25,pady=15)
btn_mi = Button(window,text="-", padx=25,pady=15)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_mi.grid(row=2,column=3)

btn_1 = Button(window,text="1", padx=25,pady=15)
btn_2 = Button(window,text="2", padx=25,pady=15)
btn_3 = Button(window,text="3", padx=25,pady=15)
btn_pl = Button(window,text="+", padx=25,pady=15)

btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)
btn_pl.grid(row=3,column=3)

btn_0 = Button(window,text="0", padx=25,pady=15)
btn_c = Button(window,text="C", padx=25,pady=15)
btn_e = Button(window,text="=", padx=25,pady=15)
btn_s = Button(window,text="/", padx=25,pady=15)

btn_0.grid(row=4,column=0)
btn_c.grid(row=4,column=1)
btn_e.grid(row=4,column=2)
btn_s.grid(row=4,column=3)




window.mainloop()