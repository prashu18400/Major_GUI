import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webcam
s = ''
age_value = 0
from webcam import webcam_capture

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def check_age(age):
    if age < 18:
        return True
    else:
        return False


def startweb():
    age_value = webcam_capture()
    if check_age(age_value):
        messagebox.showerror('Sorry!', 'You are not authorised to view the content')
    else:
        messagebox.showinfo('Wooho', 'Enjoy your show!!')


root = tk.Tk()
root.title('Content Driven Access')
root.geometry("600x400")
# button to start the webcam capture
ttk.Button(root, text="Start Webcam", command=startweb).pack()
root.mainloop()
