from tkinter import *
# ศร้างหน้าจอ
gui = Tk()
gui.geometry("1280x800")
gui.title("Test Gui python")
gui['bg']='#148CFF'
gui.resizable(0,0)
label1 = Label(gui,text="เครื่องวัดแรงกด-ดึง",font=('arial',40,'bold'),bg='#148CFF',fg='#000000', bd=10, width=40).grid(row=1,columnspan=460)
objEntry = Entry().grid(row=2, column=1000)
mbutton= Button(gui, text="MEASURE", width=8, padx=5, pady=5, bd=8,font=('arial', 10, 'bold'),bg='#1DFF00').grid(row=2, column=20)
objEntry = Entry().grid(row=4, column=1000)
mlabel = Label(text="ช่องสัญญาณ 1",font=('arial', 18, 'bold'), fg="#000",bg='#148CFF').grid(row=4, column=40)
mlabel = Label(text="ช่องสัญญาณ 2",font=('arial', 18, 'bold'), fg="#000",bg='#148CFF').grid(row=4, column=80)
mlabel = Label(text="ช่องสัญญาณ 3",font=('arial', 18, 'bold'), fg="#000",bg='#148CFF').grid(row=4, column=120)
mlabel = Label(text="ช่องสัญญาณ 4",font=('arial', 18, 'bold'), fg="#000",bg='#148CFF').grid(row=4, column=160)
mbutton= Button(gui, text="START", width=10, padx=5, pady=5, bd=20,font=('arial', 25, 'bold'),bg='#1DFF00').grid(row=5, column=380)
mbutton= Button(gui, text="11.2", width=5, bd=1,font=('arial', 40, 'bold'),bg='#C1C1C1',state='disable').grid(row=5, column=40)
mbutton= Button(gui, text="17.15", width=5, bd=1,font=('arial', 40, 'bold'),bg='#C1C1C1',state='disable').grid(row=5, column=80)
mbutton= Button(gui, text="0", width=5, bd=1,font=('arial', 40, 'bold'),bg='#C1C1C1',state='disable').grid(row=5, column=120)
mbutton= Button(gui, text="8.78", width=5, bd=1,font=('arial', 40, 'bold'),bg='#C1C1C1',state='disable').grid(row=5, column=160)
objEntry = Entry().grid(row=6, column=1000)
mlabel = Label(text="กิโลกรัม",font=('arial', 18, 'bold'), fg="#000",bg='#148CFF').grid(row=6, column=40)
mlabel = Label(text="กิโลกรัม",font=('arial', 18, 'bold'), fg="#000",bg='#148CFF').grid(row=6, column=80)
mlabel = Label(text="กิโลกรัม",font=('arial', 18, 'bold'), fg="#000",bg='#148CFF').grid(row=6, column=120)
mlabel = Label(text="กิโลกรัม",font=('arial', 18, 'bold'), fg="#000",bg='#148CFF').grid(row=6, column=160)
mbutton= Button(gui, text="STOP", width=10, padx=5, pady=5, bd=20,font=('arial', 25, 'bold'),bg='#FF0000').grid(row=7, column=380)
mbutton= Button(gui, text="ON", width=5,padx=5, pady=5, bd=10,font=('arial', 12, 'bold'),bg='#1DFF00').grid(row=7, column=40)
mbutton= Button(gui, text="ON", width=5,padx=5, pady=5, bd=10,font=('arial', 12, 'bold'),bg='#1DFF00').grid(row=7, column=80)
mbutton= Button(gui, text="OFF", width=5,padx=5, pady=5, bd=10,font=('arial', 12, 'bold'),bg='#FF0000').grid(row=7, column=120)
mbutton= Button(gui, text="ON", width=5,padx=5, pady=5, bd=10,font=('arial', 12, 'bold'),bg='#1DFF00').grid(row=7, column=160)
objEntry = Entry().grid(row=8, column=1000)
mbutton= Button(gui, text="EXPORT", width=10, padx=5, pady=5, bd=20,font=('arial', 25, 'bold'),bg='#FFCD28').grid(row=9, column=380)


gui.mainloop()
