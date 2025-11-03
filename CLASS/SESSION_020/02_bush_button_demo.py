from tkinter import *

def ok_button_handler():
    print('OK BUTTON IS CLICKED')

root_window = Tk()
root_window.title('Push Button Demo')
root_window.geometry('300x200')

ok_button = Button(root_window)
ok_button.configure(text='OK', command=ok_button_handler)
ok_button.grid(row = 0, column = 0)

print('Now Control flow goes into root_window.mainloop()')

root_window.mainloop()

print('Now get interrupt to terminate the Program')
