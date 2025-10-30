from tkinter import *

root_window = Tk()
root_window.geometry('300x150')
root_window.title('GUI Application')

msg = Label(root_window, text = 'Himanshu Kitey')
msg.grid(row = 0, column = 0)

root_window.mainloop()
