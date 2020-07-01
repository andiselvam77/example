from tkinter import *

root=Tk()
root.geometry('100x100')
def b1():
	s=e1.get()
	d=eval(s)
	label1=Label(root,text=d).pack()
e1=Entry(root)
e1.pack()
but1=Button(root,text='click',command=b1).pack()



mainloop()
