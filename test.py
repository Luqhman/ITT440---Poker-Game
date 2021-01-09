from tkinter import*
from tkinter import simpledialog

root = Tk()


def get_me():
	simpledialog.askstring()

button = Button(root,text="popup",command=get_me)
myLabel = Label(root,text="Hello world")

myLabel.pack()

root.geometry("300x300")
root.mainloop()