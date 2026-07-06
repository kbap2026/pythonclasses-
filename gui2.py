#in unit 2 we learn how to create buttons and  input fields with tikinter
from tkinter import *
# mw is main window
mw = Tk() # creating main window
# creating buttons
# we take buton ane method mw is taken as first argument or button la  and butten pina undedhi text
# my_button= Button(mw,text="Click me! ",padx=20, pady=10,font=("Arial",14))
# # button bayata padding ivalante kinda laga type cheyandi
# my_button.pack(padx=30,pady=50)


#****** creating a function to button  to execute a programme ********

# def clicked():
#     mylable = Label(mw,text="I love KBAP",font=("Arial",12))
#     mylable.pack(pady=10)
# my_button= Button(mw,text="click me! ",padx=20, pady=10,font=("Arial",14),command=clicked)# command calls function dont use arguments
# # button bayata padding ivalante kinda laga type cheyandi
# my_button.pack(padx=50,pady=30)
# like this we can use funtion in vidya varadhi

# creating input  example code *******************
# user_input= Entry(mw)
# user_input.pack()

def clicked():
    mylable = Label(mw,text="I love vidya varadhi",font=("Arial",12))
    mylable.pack(pady=10)

#*** input ****
user_input = Entry(mw,width=15,font=("Arial",18))# input pad x pani cheyadhu so widt tiskovali
user_input.pack(pady=10,)


my_button= Button(mw,text="click me! ",padx=20, pady=10,font=("Arial",14),command=clicked)# command calls function dont use arguments
# button bayata padding ivalante kinda laga type cheyandi
my_button.pack(padx=50,pady=30)
# like this we use entry method to create buttons in next tutotorials we create apps
# next tutotrials is very exiting



mw.mainloop()