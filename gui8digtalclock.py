# this tutorial is top create digital clock its a advanced level tutorials
# this a fun project using tikinter digital clock
from tkinter import *
from time import strftime
main_window =Tk()
main_window.title("Digital Clock")
main_window.geometry("630x135")# ikkada into ante x tiskovali
main_window.minsize(630,135)# standard ga resize avakunda untadhi
main_window.maxsize(630,135)# fixed size istunam
main_window.config(bg="black")# border wite lekunda vastundhundi
# creating a function to display time
def good_time():
    cur_time = strftime("%I:%M:%S %p")# this text ha a meaning you can google it
    clock_label.config(text=cur_time) # this will change the text in clock lable
    clock_label.after(1000,good_time) # dinne reccursion antam 1000 milliseconds with function rendu arguments tiskunam 100 milisec ante 1 sec
    # second kiu okasari funtion ni call chestunadu


#creating lable
clock_label = Label(main_window,text="Digital Clock",font=("Arial",80),bg="black",fg="#03fc3d",padx=5,pady=5)
clock_label.pack()

good_time() # calling the function
main_window.mainloop()

# software cheyadaniki
# pyinstaller main.py -i clock.ico -F -w