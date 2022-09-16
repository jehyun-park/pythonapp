from tkinter import *

window = Tk()
window.title("제목없음")
window.geometry("640x480")

btn_num = Button(window,text="Num Lock", width=10,height=3,padx=10,pady=10)
btn_s = Button(window,text="/", padx=10,pady=10, width=10,height=3)
btn_m = Button(window,text="*", padx=10,pady=10, width=10,height=3)
btn_mi = Button(window,text="-", padx=10,pady=10, width=10,height=3)

btn_num.grid(row=0,column=0, sticky=N+E+W+S)
btn_s.grid(row=0,column=1, sticky=N+E+W+S)
btn_m.grid(row=0,column=2, sticky=N+E+W+S)
btn_mi.grid(row=0,column=3, sticky=N+E+W+S)

btn_7 = Button(window,text="7", padx=10,pady=10, width=10,height=3)
btn_8 = Button(window,text="8", padx=10,pady=10, width=10,height=3)
btn_9 = Button(window,text="9", padx=10,pady=10, width=10,height=3)
btn_pl = Button(window,text="+", padx=10,pady=10, width=10,height=3)

btn_7.grid(row=1,column=0, sticky=N+E+W+S, padx=3,pady=2)
btn_8.grid(row=1,column=1, sticky=N+E+W+S, padx=3,pady=2)
btn_9.grid(row=1,column=2, sticky=N+E+W+S, padx=3,pady=2)
btn_pl.grid(row=1,column=3, rowspan=2, sticky=N+E+W+S, padx=3,pady=2)

btn_4 = Button(window,text="4", padx=10,pady=10, width=10,height=3)
btn_5 = Button(window,text="5", padx=10,pady=10, width=10,height=3)
btn_6 = Button(window,text="6", padx=10,pady=10, width=10,height=3)

btn_4.grid(row=2,column=0, sticky=N+E+W+S, padx=3,pady=2)
btn_5.grid(row=2,column=1, sticky=N+E+W+S, padx=3,pady=2)
btn_6.grid(row=2,column=2, sticky=N+E+W+S, padx=3,pady=2)

btn_1 = Button(window,text="1", padx=10,pady=10, width=10,height=3)
btn_2 = Button(window,text="2", padx=10,pady=10, width=10,height=3)
btn_3 = Button(window,text="3", padx=10,pady=10, width=10,height=3)
btn_en = Button(window,text="Enter", padx=10,pady=10, width=10,height=3)

btn_1.grid(row=3,column=0, sticky=N+E+W+S, padx=3,pady=2)
btn_2.grid(row=3,column=1, sticky=N+E+W+S, padx=3,pady=2)
btn_3.grid(row=3,column=2, sticky=N+E+W+S, padx=3,pady=2)
btn_en.grid(row=3,column=3, rowspan=2, sticky=N+E+W+S, padx=3,pady=2)

btn_0 = Button(window,text="0", padx=10,pady=10, width=10,height=3)
btn_dot = Button(window,text=".", padx=10,pady=10, width=10,height=3)

btn_0.grid(row=4,column=0,columnspan=2, sticky=N+E+W+S, padx=3,pady=2)
btn_dot.grid(row=4,column=2,sticky=N+E+W+S, padx=3,pady=2)




window.mainloop()