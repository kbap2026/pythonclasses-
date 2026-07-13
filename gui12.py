# in this lession i will teach yoou how to create windows
# multiple windows
# till know we have used main window only know onwards we will lear how to use 2 windouws or multiple windows
from tkinter import *
from PIL import Image, ImageTk

main_window = Tk()

main_window.title("main window ")
main_window.geometry("400x300")
img = ""
def open_window():
    global img
    second_window = Toplevel() # it will create second window
    second_window.title(" this is second window ")

    #second_window.geometry("700x500")
    img= ImageTk.PhotoImage(Image.open("images/1.jpg"))
    img_label = Label(second_window,image=img)
    img_label.pack(padx=10, pady=10)
    exit_btn = Button(second_window,text="exit window",font=("",16),command=second_window.destroy)
    exit_btn.pack(padx=20,pady=20)


ow_btn = Button(main_window,text="open window",font=("",16),command=open_window)
ow_btn.pack(pady=(60,0))
main_window.mainloop()