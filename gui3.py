# create say hellow gui app  we learn in this
from tkinter import *
mw = Tk()

#
# userinput = Entry(mw)  # using entry method
# userinput.pack() # this looks ugly
#
# mw.mainloop()  # app created



# we are creating a new design for the app

# userinput = Entry(mw, width=20,font=('Arial', 18))
# userinput.pack(padx=10, pady=10) # tis is to write my name
# # dinikinda oka label anedi kavali i create it now
# text = Label(mw, text="Enter your name", font=("Arial", 14)) # text field create ayindhi
# # pidanni screen ki add cheyali
# text.pack()# run chesi chuste enter your name ani vachesindhi
#
# mw.mainloop()  # app created








# userinput = Entry(mw, width=20,font=('Arial', 18))
# userinput.pack(padx=10, pady=10) # tis is to write my name
# # dinikinda oka label anedi kavali i create it now
# text = Label(mw, text="Enter your name!", font=("Arial", 14)) # text field create ayindhi
# # pidanni screen ki add cheyali
# text.pack(pady=5)# run chesi chuste enter your name ani vachesindhi
# #
# # # i want to create a button
# btn =Button(mw, text="say hello", font=("Arial" , 12)) # to add it to screen
# btn.pack(pady=20) # button is working # i need to create space in top and bottom
# mw.mainloop()  # app created

## ippudui daka button and anni create chesam but emi pani cheyatledu ippudu dinni oka funtion tho app la marchukuntam
## chandu ani enter chesi say hello button nokkite hello w chandu ani ravali

#
# def say_hello():
#     name = userinput.get()
#     greeting = "Hello "+ name + "!"
#     text.config(text=greeting)    # label ni ower write cheyadaniki
#
# userinput = Entry(mw, width=20,font=('Arial', 18))
# userinput.pack(padx=10, pady=10) # tis is to write my name
# # dinikinda oka label anedi kavali i create it now
# text = Label(mw, text="Enter your name!", font=("Arial", 14)) # text field create ayindhi
# # pidanni screen ki add cheyali
# text.pack(pady=5)# run chesi chuste enter your name ani vachesindhi
#
# # i want to create a button
# btn =Button(mw, text="say hello", font=("Arial" , 12), command=say_hello) # to add it to screen // say hellow anedi function name
# btn.pack(pady=20) # button is working # i need to create space in top and bottom
# mw.mainloop()  # app created



## user edi enter cheste adi input vastadhihello w chandu ani
## say hello w anedi  just emi enter cheyakapote hellow vastadhi  idi ok anukunte uncheyandi
#
# def say_hello():
#     name = userinput.get()
#     greeting = "Hello "+ name + "!"
#     text.config(text=greeting)    # label ni ower write cheyadaniki
#
# userinput = Entry(mw, width=20,font=('Arial', 18))
# userinput.pack(padx=10, pady=10) # tis is to write my name
# # dinikinda oka label anedi kavali i create it now
# text = Label(mw, text="Enter your name!", font=("Arial", 14)) # text field create ayindhi
# # pidanni screen ki add cheyali
# text.pack(pady=5)# run chesi chuste enter your name ani vachesindhi
#
# # i want to create a button
# btn =Button(mw, text="say hello", font=("Arial" , 12), command=say_hello) # to add it to screen // say hellow anedi function name
# btn.pack(pady=20) # button is working # i need to create space in top and bottom
# mw.mainloop()  # app created
#






#name enter cheyakapote hellow ani rakudadhu ante

def say_hello():
    name = userinput.get()
    greeting = "Hello "+ name + "!"
    if name != "":
        text.config(text=greeting)
        userinput.delete(0, END) # enter chese text input lo povalante
    #text.config(text=greeting)    # label ni ower write cheyadaniki

userinput = Entry(mw, width=20,font=('Arial', 18))
userinput.pack(padx=10, pady=10) # tis is to write my name
# dinikinda oka label anedi kavali i create it now
text = Label(mw, text="Enter your name!", font=("Arial", 14)) # text field create ayindhi
# pidanni screen ki add cheyali
text.pack(pady=5)# run chesi chuste enter your name ani vachesindhi

# i want to create a button
btn =Button(mw, text="say hello", font=("Arial" , 12), command=say_hello) # to add it to screen // say hellow anedi function name
btn.pack(pady=20) # button is working # i need to create space in top and bottom
mw.mainloop()  # app created

# ye python file ni soft ware laga marchali
# because the output will come as a console
# so take a pyinstaller filename.py --noconsole --onefile
# bundling
# dist lo file untatadhi say hellow ani 
