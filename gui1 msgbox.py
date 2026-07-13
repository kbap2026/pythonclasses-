from tkinter import *
from tkinter import messagebox

main_window = Tk()
main_window.title("message boxes ")
#main_window.iconbitmap("icon.ico")
main_window.geometry("400x300")

def show_msg():
    # messagebox.showinfo("this is a message box",'VIDYA VARADHI')
    #messagebox.showwarning("this is a message box", 'VIDYA VARADHI')
    #res= messagebox.showerror("this is a message box", 'VIDYA VARADHI')
    #res = messagebox.askyesno("this is a message box", 'VIDYA VARADHI')
    #res = messagebox.askquestion("this is a message box", 'VIDYA VARADHI')
    #res = messagebox.askokcancel("this is a message box", 'VIDYA VARADHI')
    res = messagebox.askquestion("this is a message box", 'Do you want to save file ?')
    if res == "yes": # pi question adidigetapudu label  lo text = degra res ani peti vadileandi
        Label(main_window,text="File has been saved!",font=("",16)).pack(pady=(20,0))
    else:
        messagebox.showwarning("This is a msg box ", " your file has been trashed ")

Button(main_window,text="show message!",font=("",16),command=show_msg).pack(pady=(50,0))




main_window.mainloop()